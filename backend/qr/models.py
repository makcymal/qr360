from django.db import models


class User(models.Model):
	phone 		  = models.CharField(max_length=12)
	password_hash = models.CharField(max_length=64, default="")

	def __str__(self):
		return self.phone


class Session(models.Model):
	user 		 = models.ForeignKey(User, on_delete=models.CASCADE)
	session_hash = models.CharField(max_length=64)
		
	def __str__(self):
		return str(user)
