from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Advertisment(models.Model):
	AdID	= models.IntegerField(primary_key=True)
	Name	= models.CharField(max_length=256)
	Path	= models.CharField(max_length=256)
	InDate	= models.DateTimeField('Date of Insertion')
	ExpDate	= models.DateTimeField('Date of Expiry')
	DTemp	= models.IntegerField()
	CHOICES_Cond = ((0,'MIST'),(1,'CLOUDS'),(2,'CLEAR'),(3,'RAIN'))
	DCond	= models.IntegerField(choices=CHOICES_Cond)
	DWind	= models.FloatField()
	DHumidity = models.IntegerField()
	Rel	= models.IntegerField(default=0)

	def __unicode__(self):
		return self.Name

class Authentication(models.Model):
	pi_name	= models.CharField(max_length=100,primary_key=True)
	in_use	= models.BooleanField(default=False)
	uniq_id	= models.CharField(max_length=100)

	def __unicode__(self):
		return self.pi_name

class Disruption(models.Model):
	DisruptID	= models.IntegerField(primary_key=True)
	CHOICES_Service	= ((0,'TRAM'),(1,'BUS'),(2,'TRAIN'))
	Service		= models.IntegerField(choices=CHOICES_Service)
	Route		= models.IntegerField()
	CHOICES_Duration= ((0,'CONTINUOUS'),(1,'DISCRETE'),(2,'INDEFINITE'))
	Duration	= models.IntegerField(choices=CHOICES_Duration) 
	CHOICES_Disrupt	= ((0,'RELOCATION'),(1,'DIVERSION'),(2,'CLOSURE'))
	Disrupt		= models.IntegerField(choices=CHOICES_Disrupt)

class ServiceLocation(models.Model):
	SerLocID	= models.IntegerField(primary_key=True)
	CHOICES_Service = ((0,'TRAM'),(1,'BUS'),(2,'TRAIN'))
	ServiceType	= models.IntegerField(choices=CHOICES_Service)
	Route		= models.IntegerField()
	Location	= models.CharField(max_length=256)

class Weather(models.Model):
	LocID		= models.IntegerField(primary_key=True)
	Temp		= models.IntegerField()
	CHOICES_Cond	= ((0,'MIST'),(1,'CLOUDS'),(2,'CLEAR'),(3,'RAIN'))
	Cond		= models.IntegerField(choices=CHOICES_Cond)
	Wind		= models.FloatField()
	Humidity	= models.IntegerField()

class Location(models.Model):
	LocID	= models.IntegerField(primary_key=True)
	Name	= models.CharField(max_length=256)
	GPS_Lat = models.FloatField()
	GPS_Long= models.FloatField()

	def __unicode__(self):
		return self.Name
