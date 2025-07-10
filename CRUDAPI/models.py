from django.db import models

# Create your models here.

class TMSys(models.Model):
    TaskId= models.AutoField(primary_key=True)
    TaskTitle=models.CharField(max_length=500)
    TaskDescription=models.CharField(max_length=500)
    TaskDuedate=models.DateTimeField()

class Users(models.Model):
    UserId=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=500)
    UserEmail=models.CharField(max_length=500)
    Task=models.CharField(max_length=500)

