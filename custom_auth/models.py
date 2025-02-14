from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
	email_or_phone=models.CharField(max_length=50, unique=True, verbose_name='Email or Phone')
	username=None
	email=None
	first_name=models.CharField(max_length=20, blank=True, null=True)
	last_name=models.CharField(max_length=20, blank=True, null=True)
	
	USERNAME_FIELD='email_or_phone'
	REQUIRED_FIELDS=[]

	class custom_manager(BaseUserManager):
		def create_user(self, email_or_phone, password):
			user = self.model(
			email_or_phone=email_or_phone
			)
			user.set_password(password)
			user.save()
			return user
		def create_superuser(self, email_or_phone, password):
			user = self.create_user(
			email_or_phone=email_or_phone,
			password=password,
			)
			user.is_staff = True
			user.is_superuser = True
			user.is_buyer = None
			user.save()
			return user
	

	objects=custom_manager()