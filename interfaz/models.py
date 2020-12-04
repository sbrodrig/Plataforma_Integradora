from django.db import models

# Create your models here.

class Rbdms(models.Model):
	name = models.CharField(max_length=15)
	def __str__():
		return self.name


class HardwareType(models.Model):
	name = models.CharField(max_length=10)
	specifications = models.CharField(max_length=1000)
	def __str__(self):
		return self.name


class OSType(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name


class Test(models.Model):
	rdbms = models.ForeignKey(Rbdms)
	hw_type = models.ForeignKey(HardwareType)
	hw_spec = models.CharField(max_length=1000)
	os_type = models.ForeignKey(OSType)