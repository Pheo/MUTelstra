from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Advertisment(models.Model):
	AdID	= models.AutoField(primary_key=True)
	Name	= models.CharField(max_length=256)
	Path	= models.CharField(max_length=256)
	InDate	= models.DateTimeField('Date of Insertion')
	ExpDate	= models.DateTimeField('Date of Expiry')
	DTemp	= models.IntegerField()
	CHOICES_Cond = ((0,'MIST'),(1,'CLOUDS'),(2,'CLEAR'),(3,'RAIN'))
	DCond	= models.IntegerField(choices=CHOICES_Cond)
	DWind	= models.FloatField()
	DHumidity = models.IntegerField()
	DTime	= models.TimeField()
	BidAmt	= models.FloatField()
	MaxBdgt	= models.FloatField()
	RelVar	= models.IntegerField()
	Rel	= models.IntegerField(default=0)

	def __unicode__(self):
		return self.Name

class Authentication(models.Model):
	pi_name	= models.CharField(max_length=100,primary_key=True)
	in_use	= models.BooleanField(default=False)
	uniq_id	= models.CharField(max_length=100)

	def __unicode__(self):
		return self.pi_name

class Weather(models.Model):
	LocID		= models.IntegerField(primary_key=True)
	Temp		= models.IntegerField()
	CHOICES_Cond	= ((0,'MIST'),(1,'CLOUDS'),(2,'CLEAR'),(3,'RAIN'))
	Cond		= models.IntegerField(choices=CHOICES_Cond)
	Wind		= models.FloatField()
	Humidity	= models.IntegerField()

class Location(models.Model):
	LocID	= models.AutoField(primary_key=True)
	CityID	= models.IntegerField()
	GPS_Lat = models.FloatField()
	GPS_Long= models.FloatField()
