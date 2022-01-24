from django.db import models


class adddatamod(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    fee= models.IntegerField()
    assignment1=models.IntegerField()
    assignment2=models.IntegerField()
    assignment3=models.IntegerField()
    assignment4=models.IntegerField()
    total = models.IntegerField()
    avg= models.IntegerField()


