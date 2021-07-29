from django.db import models


class info(models.Model):
	name=models.CharField(max_length=50)
	photo=models.ImageField(upload_to='image', blank=True)
	intro_line=models.CharField(max_length=50, blank=True)
	designation=models.CharField(max_length=40)
	resume=models.FileField(upload_to='resume',blank=True)
	about=models.TextField(blank=True)
	phone=models.BigIntegerField()
	email=models.EmailField()
	github=models.URLField(blank=True)

	def __str__(self):
		return self.name


class project(models.Model):
	name=models.CharField(max_length=30)
	github_link=models.URLField()
	description=models.TextField()
	image=models.ImageField(upload_to='image', blank=True)

	def __str__(self):
		return self.name

