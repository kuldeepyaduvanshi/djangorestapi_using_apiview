from django.db import models

# Create your models here.

class Restorent(models.Model):
	name = models.CharField(max_length=30)
	city = models.CharField(max_length=20)
	famous_for = models.CharField(max_length=30)
	owner = models.CharField(max_length=20)

	def __str__(self):
		return self.name

