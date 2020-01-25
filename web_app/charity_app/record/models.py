from django.db import models

class Record(models.Model):
	charity = models.CharField('Charity', max_length=120)
	item = models.CharField(max_length=120)
	time = models.CharField(max_length=120)
	location = models.CharField(max_length = 60)