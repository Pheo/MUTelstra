from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Advertisment(models.Model):
	ad_id	= models.IntegerField(primary_key=True)
	date	= models.DateTimeField('date published')
	expiry	= models.DateTimeField('date of expiry')
	CHOICES_pt = ((0,'NORMAL'),(1,'DELAY'),(2,'SEVERE_DELAYS'))
	pt	= models.IntegerField(choices=CHOICES_pt,default=0)
	pt_ba	= models.FloatField(
		validators=[MinValueValidator(0.1)])
	CHOICES_w = ((0,'SHOWERS'),(1,'RAINING'),(2,'CLOUDY'),(3,'SUNNY'))
	w_con	= models.IntegerField(choices=CHOICES_w,default=0)
	w_con_ba= models.FloatField(
		validators=[MinValueValidator(0.1)])
	w_tem	= models.IntegerField( 
		validators=[MinValueValidator(-10),MaxValueValidator(50)])
	w_tem_ba= models.FloatField(
		validators=[MinValueValidator(0.1)])
	dt	= models.IntegerField(
		validators=[MinValueValidator(0),MaxValueValidator(23)])
	dt_ba	= models.FloatField(
		validators=[MinValueValidator(0.1)])
	name	= models.CharField(max_length=32)
	path	= models.CharField(max_length=256)
	rel	= models.IntegerField(default=0)

class Authentication(models.Model):
	pi_name	= models.CharField(max_length=100,primary_key=True)
	in_use	= models.BooleanField(default=False)
	uniq_id	= models.CharField(max_length=100)

class Disruption(models.Model):
	dis_id	= models.IntegerField(primary_key=True)
	CHOICES_ser = ((0,'TRAM'),(1,'BUS'),(2,'TRAIN'))
	ser_type= models.IntegerField(choices=CHOICES_ser,default=0)
	route	= models.IntegerField()
	CHOICES_duration = ((0,'CONTINUOUS'),(1,'DISCRETE'),(2,'INDEFINITE'))
	duration= models.IntegerField(choices=CHOICES_duration) 
	CHOICES_disrupt = ((0,'RELOCATION'),(1,'DIVERSION'),(2,'CLOSURE'))
	disrupt	= models.IntegerField(choices=CHOICES_disrupt)

class ServiceLocation(models.Model):
	CHOICES_ser = ((0,'TRAM'),(1,'BUS'),(2,'TRAIN'))
	ser_type= models.IntegerField(choices=CHOICES_ser,default=0)
	route	= models.IntegerField()
	location= models.CharField(max_length=256)
