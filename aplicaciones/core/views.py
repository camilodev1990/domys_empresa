from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import logout
from django.views import View
from django.views.generic.edit import CreateView
from .forms import ConfirmPasswordForm, CustomLoginForm, CustomPasswordChangeForm, SignUpForm, CustomPasswordResetForm
from .decorators import terminos_aceptados
from .forms import TerminosYCondicionesForm
from .models import TerminosYCondiciones, UsuarioInactivo, ListaNegra



#---------------------------------------------------------------------------------------------------------
#vista base
def base(request):
    return render(request, 'base.html')

#---------------------------------------------------------------------------------------------------------
#vista terminos y condiciones
@login_required
def terminosycondiciones(request):
    # Intentar obtener una instancia existente del modelo TerminosYCondiciones para el usuario
    try:
        termino = TerminosYCondiciones.objects.get(usuario=request.user)
    except TerminosYCondiciones.DoesNotExist:
        # Si no existe, crear una instancia vacía
        termino = TerminosYCondiciones(usuario=request.user)

    if request.method == 'POST':
        form = TerminosYCondicionesForm(request.POST, instance=termino)
        if form.is_valid():
            # Actualizar el campo 'aceptado' con el valor del formulario
            form.save()
            # Redirigir a otra página o mostrar un mensaje de éxito
            return redirect('base')  # Cambia esto según tu necesidad
    else:
        form = TerminosYCondicionesForm(instance=termino)

    return render(request, 'terminos.html', {'form': form})

#---------------------------------------------------------------------------------------------------------
#vista ingreso
class CustomLoginView(LoginView):
    form_class = CustomLoginForm

#---------------------------------------------------------------------------------------------------------
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # Utiliza reverse_lazy para que sea más seguro y dinámico
    template_name = 'signup.html'

#---------------------------------------------------------------------------------------------------------
#vista confirmar cerrar sesion
@method_decorator(login_required, name='dispatch')
class ConfirmLogoutView(View):
    template_name = 'confirm_logout.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        return redirect('base')
    
#---------------------------------------------------------------------------------------------------------
#vista para recuperar contraseña
def custom_password_reset(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('password_reset_done')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})

#---------------------------------------------------------------------------------------------------------
#vista para eliminar cuenta
@login_required
def delete_account(request):
    if request.method == 'POST':
        form = ConfirmPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = authenticate(username=request.user.username, password=password)
            if user is not None:
                # Marcar el usuario como inactivo
                user.is_active = False
                user.save()

                # Mover a la tabla de usuarios inactivos
                UsuarioInactivo.objects.create(
                    email=user.email,
                    username=user.username
                )

                messages.success(request, 'Cuenta inactivada exitosamente.')
                return redirect('base')
            else:
                messages.error(request, 'Contraseña incorrecta. Por favor, inténtelo de nuevo.')
    else:
        form = ConfirmPasswordForm()
    
    return render(request, 'delete_account.html', {'form': form})

#---------------------------------------------------------------------------------------------------------
# Vista para cambiar la contraseña
@method_decorator(login_required, name='dispatch')
#@method_decorator(terminos_aceptados(redirect_url='terminos'), name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        messages.success(self.request, 'Tu contraseña ha sido actualizada exitosamente.')
        return super().form_valid(form)

#---------------------------------------------------------------------------------------------------------

