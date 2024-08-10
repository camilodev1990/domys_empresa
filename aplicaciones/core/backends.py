from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import ListaNegra

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) and user.is_active and not ListaNegra.objects.filter(username=username).exists():
                return user
        except User.DoesNotExist:
            return None
        return None