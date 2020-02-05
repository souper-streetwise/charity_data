from django.db import models

class Item(models.Model):
	item = models.CharField(max_length=120)

	def __str__(self):
		return self.item

class Record(models.Model):
	charity = models.CharField('Charity', max_length=120)
#	item = models.CharField(max_length=120)
#	time = models.CharField(max_length=120)
	time = models.DateTimeField(auto_now_add=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
#	time = models.DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])
	location = models.CharField(max_length = 60)



