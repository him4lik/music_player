from django.db import models
from custom_auth.models import User
from django.contrib.auth.models import AnonymousUser

#Song model
class song(models.Model):
	name=models.CharField(max_length=50)
	audio=models.FileField(upload_to="audio")
	artist=models.CharField(max_length=30)
	liked_by=models.ManyToManyField(User, related_name='liked_songs', blank=True)

	def __str__(self):
		return self.name

		
#Playlist model
class playlist(models.Model):
	name=models.CharField(max_length=50)
	songs=models.ManyToManyField(song)
	user=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
