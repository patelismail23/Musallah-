from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Musallah (models.Model):
	musallah_name = models.CharField(max_length=200)
	pincode = models.IntegerField()
	area = models.CharField(max_length=200)
	street = models.CharField(max_length=200)
	landmark = models.CharField(max_length=100)
	contact_no= models.BigIntegerField()
	maslak = models.CharField(max_length=20)
	is_musallah = models.BooleanField(default=False)
	distance_near_stn=models.FloatField()
	musallah_lat = models.FloatField()	
	musallah_lng = models.FloatField()
	is_verified = models.BooleanField(default=False)

class Users(models.Model):
	user_name = models.CharField(max_length=50)
	user_loc_lat = models.FloatField()
	user_loc_lng = models.FloatField()
	user_contact =  models.BigIntegerField()
	user_area = models.CharField(max_length=200)
	user_pincode = models.IntegerField()
	is_verified = models.BooleanField(default=False)
	
class NamazTiming(models.Model):
	namaz_fajr = models.DateTimeField()	
	namaz_zuhr = models.DateTimeField()
	namaz_asr = models.DateTimeField()
	namaz_magrib = models.DateTimeField()
	namaz_isha = models.DateTimeField()
	namaz_jummah = ArrayField(models.DateTimeField())
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	

class Facilities(models.Model):
	musullah_fk = models.ForeignKey(Musallah,on_delete=models.CASCADE)
	is_jummah_avail = models.BooleanField(default=True)
	is_wuzu_avail = models.BooleanField(default=True)
	is_women_facility = models.BooleanField(default=False)
	is_parking_avail = models.BooleanField(default=False)


class RamzanTiming(models.Model):
	musullah_fk = models.ForeignKey(Musallah,on_delete=models.CASCADE)
	taravih_time = ArrayField(models.DateTimeField())
	eid_time = ArrayField(models.DateTimeField())
	is_iftar_avail = models.BooleanField(default=True)

	 
class HasBeen(models.Model):
	musallah_fk = models.ForeignKey(Musallah,on_delete=models.CASCADE)
	user_fk = models.ForeignKey(Users,on_delete=models.CASCADE)
	upvotes = models.IntegerField()
