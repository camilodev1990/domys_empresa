from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string

@receiver(post_save, sender=User)
def enviar_correo_bienvenida(sender, instance, created, **kwargs):
    if created:
        subject = 'Bienvenido a nuestro sitio'
        message = render_to_string('emails/bienvenida.html', {
            'user': instance,
        })
        send_mail(subject, message, settings.EMAIL_HOST_USER, [instance.email], fail_silently=False)


