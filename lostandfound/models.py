from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class LostPet(models.Model):
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	animal_lost = models.CharField(max_length=50)
	location_lost = models.CharField(max_length=30)
	description_lost = models.TextField()
	reward_pet_lost = models.CharField(max_length=5)
	date_lost = models.DateField()
	post_date_lost = models.DateTimeField(default=timezone.now)
	number_lost = models.BigIntegerField()
	picture_lost =  models.ImageField(upload_to="media",verbose_name="Image", blank=True, null=True)
	

class FoundPet(models.Model):
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	animal_found = models.CharField(max_length=50)
	location_found = models.CharField(max_length=30)
	description_found = models.TextField()
	date_found = models.DateField()
	post_date_found = models.DateTimeField(default=timezone.now)
	number_found = models.BigIntegerField()
	picture_found =  models.ImageField(upload_to="media",verbose_name="Image", blank=True, null=True)



class LostObject(models.Model):
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	obj_item_lost = models.CharField(max_length=50)
	obj_date_lost = models.DateField()
	obj_location_lost = models.CharField(max_length=50)
	obj_description_lost = models.CharField(max_length=100)
	obj_picture_lost = models.ImageField(upload_to="media",verbose_name="Image", blank=True, null=True)
	obj_reward_lost = models.CharField(max_length=5)
	obj_number_lost = models.CharField(max_length=50)
	o_post_date_lost = models.DateTimeField(default=timezone.now)


class FoundObject(models.Model):
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	obj_item_found = models.CharField(max_length=50)
	obj_date_found = models.DateField()
	obj_location_found = models.CharField(max_length=50)
	obj_description_found = models.CharField(max_length=100)
	obj_picture_found = models.ImageField(upload_to="media",verbose_name="Image", blank=True, null=True)
	obj_number_found = models.CharField(max_length=50)
	o_post_date_found = models.DateTimeField(default=timezone.now)


class LostPerson(models.Model):
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	per_name_lost = models.CharField(max_length=50)
	per_date_lost = models.DateField()
	per_location_lost = models.CharField(max_length=50)
	per_description_lost = models.CharField(max_length=100)
	per_picture_lost = models.ImageField(upload_to="media",verbose_name="Image", blank=True, null=True)
	per_number_lost = models.CharField(max_length=50)
	per_post_date_lost = models.DateTimeField(default=timezone.now)
	per_age_lost = models.IntegerField()
	per_gender_lost = models.CharField(max_length=50)
	per_reward_lost = models.CharField(max_length=5, null=True)

class FoundPerson(models.Model):
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	per_name_found = models.CharField(max_length=50)
	per_date_found = models.DateField()
	per_location_found = models.CharField(max_length=50)
	per_description_found = models.CharField(max_length=100)
	per_picture_found = models.ImageField(upload_to="media",verbose_name="Image", blank=True, null=True)
	per_number_found = models.CharField(max_length=50)
	per_post_date_found = models.DateTimeField(default=timezone.now)
	per_age_found = models.IntegerField()
	per_gender_found = models.CharField(max_length=50)


