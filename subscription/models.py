from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import time

STATE_CHOICES = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),   
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    age = models.IntegerField()
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)


class Monthly_plan(models.Model):
    plan_type=models.CharField(max_length=200)
    price=models.IntegerField()
    quality=models.CharField(max_length=200)
    resolution=models.CharField(max_length=200)
    allow_devices=models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

class Yearly_plan(models.Model):
    plan_type=models.CharField(max_length=200)
    price=models.IntegerField()
    quality=models.CharField(max_length=200)
    resolution=models.CharField(max_length=200)
    allow_devices=models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

class Purchased_plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_type=models.CharField(max_length=200)
    price=models.IntegerField()
    allow_devices=models.CharField(max_length=200)
    yr_mon=models.CharField(max_length=200,default='mon')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.id)

class Cancelled_plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_type=models.CharField(max_length=200)
    price=models.IntegerField()
    allow_devices=models.CharField(max_length=200)
    yr_mon=models.CharField(max_length=200,default='mon')
    cancelled_date = models.DateField()

    def __str__(self):
        return str(self.id)



           



