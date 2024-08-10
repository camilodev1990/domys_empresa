from django.db import models
from django.contrib.auth.models import User


#---------------------------------------------------------------------------------------------------------
#modelo de terminos y condiciones aceptados
class TerminosYCondiciones(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    aceptado = models.BooleanField(default=False, verbose_name='Aceptado')
    aceptado_en = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de aceptación')
    modificado_en = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def __str__(self):
        return f"Términos aceptados: {'Sí' if self.aceptado else 'No'}"
    
    class Meta:
        db_table = 'terminos_y_condiciones' 
        verbose_name = 'Término y Condición'  
        verbose_name_plural = 'Términos y Condiciones'  
        ordering = ['-id']  
#---------------------------------------------------------------------------------------------------------

# Modelo de usuario inactivo
class UsuarioInactivo(models.Model):
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    username = models.CharField(max_length=150, unique=True, verbose_name='Nombre de Usuario')
    fecha_inactivacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Inactivación')

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        db_table = 'usuario_inactivo'
        verbose_name = 'Usuario Inactivo'
        verbose_name_plural = 'Usuarios Inactivos'
        ordering = ['-fecha_inactivacion']
    
#---------------------------------------------------------------------------------------------------------

# Modelo de lista negra
class ListaNegra(models.Model):
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    username = models.CharField(max_length=150, unique=True, verbose_name='Nombre de Usuario')
    fecha_adicion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Adición')

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        db_table = 'lista_negra'
        verbose_name = 'Lista Negra'
        verbose_name_plural = 'Listas Negras'
        ordering = ['-fecha_adicion']
    
#---------------------------------------------------------------------------------------------------------