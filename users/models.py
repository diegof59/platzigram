from django.db import models
from django.contrib.auth.models import User

 
class Profile(models.Model):
    """ Representa el perfil de un usuario. Se relaciona 1-1 con la clase User que provee django """
    # Relacion 1-1:
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    web_site = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True)
    date_modified = models.DateTimeField(auto_now=True)

    profile_picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    def __str__(self):
        """Representacion string, retorna username."""
        return self.user.username
