from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

	title = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='posts/photos')
	
	created = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)               
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
	
	def __str__(self):
	
		return '{} by @{}'.format(self.title, self.user.username)