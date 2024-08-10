from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import TerminosYCondiciones, UsuarioInactivo, ListaNegra

# Personalizar el UserAdmin
class UserAdmin(BaseUserAdmin):
    # Mostrar campos en la vista de lista
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    
    # Mostrar campos en el formulario de edición
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Fechas', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Mostrar campos en el formulario de creación
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
    # Configurar filtros en la vista de lista
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'date_joined')

# Registrar el UserAdmin personalizado
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



@admin.register(TerminosYCondiciones)
class TerminosYCondicionesAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'aceptado', 'aceptado_en', 'modificado_en')
    list_filter = ('aceptado', 'aceptado_en')
    search_fields = ('usuario__username', 'usuario__email')
    readonly_fields = ('aceptado_en', 'modificado_en')

@admin.register(UsuarioInactivo)
class UsuarioInactivoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'fecha_inactivacion')
    search_fields = ('username', 'email')
    readonly_fields = ('fecha_inactivacion',)

@admin.register(ListaNegra)
class ListaNegraAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'fecha_adicion')
    search_fields = ('username', 'email')
    readonly_fields = ('fecha_adicion',)
