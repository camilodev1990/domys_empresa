from django.shortcuts import redirect
from functools import wraps


# decorador de terminos y condiciones
def terminos_aceptados(redirect_url):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.terminosycondiciones.aceptado:
                return redirect(redirect_url)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
