from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Advertisment(models.Model):
	AdID	= models.AutoField(primary_key=True)
	Name	= models.CharField(max_length=256)
	Path	= models.CharField(max_length=256)
	InDate	= models.DateTimeField('Date of Insertion')
	ExpDate	= models.DateTimeField('Date of Expiry')
	DTemp	= models.IntegerField(null=True)
	CHOICES_Cond = ((0,'MIST'),(1,'CLOUDS'),(2,'CLEAR'),(3,'RAIN'))
	DCond	= models.IntegerField(choices=CHOICES_Cond, null=True)
	DWind	= models.FloatField(null=True)
	DHumidity = models.IntegerField(null=True)
	DTime	= models.IntegerField(null=True)
	BidAmt	= models.FloatField()
	MaxBdgt	= models.FloatField()
	RelVar	= models.IntegerField()
	Rel	= models.IntegerField(default=0)
	RelMin	= models.IntegerField()
	AdTime	= models.IntegerField()
	MinIter	= models.IntegerField()
	MaxIter	= models.IntegerField()
	AdvertiserID = models.IntegerField()

	def __unicode__(self):
		return self.Name

class Advertiser(models.Model):
	AdvertiserID = models.AutoField(primary_key=True)
	Username     = models.CharField(max_length=256)
	Password     = models.CharField(max_length=256)
	MaxAllowance = models.FloatField()
	CurrentUsage = models.FloatField()
	BillingDate  = models.FloatField()
	Penalties    = models.FloatField()


class Authentication(models.Model):
	pi_name	= models.CharField(max_length=100,primary_key=True)
	in_use	= models.BooleanField(default=False)
	uniq_id	= models.CharField(max_length=100)
	LocID	= models.IntegerField()
	IPAddr	= models.CharField(max_length=100)

	def __unicode__(self):
		return self.pi_name

class AdLocation (models.Model):
	AdLocID	= models.AutoField(primary_key=True)
	pi_name = models.CharField(max_length=100)
	AdID	= models.IntegerField()	

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
	Name	= models.CharField(max_length=100)

class TrivialWeather(models.Model):
	CHOICES_Season = ((0,'SPRING'),(1,'SUMMER'),(2,'AUTUMN'),(3,'WINTER'))
	Season	= models.IntegerField(choices=CHOICES_Season,primary_key=True)
	TempAVG = models.FloatField()
	TempLQ	= models.FloatField()
	TempHQ	= models.FloatField()
	MistP	= models.IntegerField()
	CloudsP	= models.IntegerField()
	ClearP	= models.IntegerField()
	RainP	= models.IntegerField()
	HumidityAVG = models.IntegerField()
	HumidityHQ  = models.IntegerField()
	HumidityLQ  = models.IntegerField()
	WindAVG	= models.FloatField()
	WindHQ	= models.FloatField()
	WindLQ	= models.FloatField()
