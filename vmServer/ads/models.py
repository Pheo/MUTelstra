from django.db import models

# Create your models here.
class Advertisment(models.Model):
	ad_id	= models.IntegerField(primary_key=True)
	title	= models.CharField(max_length=100)
	message	= models.CharField(max_length=1000)
	date	= models.DateTimeField('date published')
