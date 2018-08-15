from django.db import models

# Create your models here.


# Model: User
class User(models.Model):

	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=90)
	bio = models.TextField()
	birth_date = models.DateField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	is_admin = models.BooleanField(default=True)
	
