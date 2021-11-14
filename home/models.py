from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=22)
    fathersname=models.CharField(max_length=100)
class catagory(models.Model):
    catagory_name=models.CharField(max_length=100)
class book(models.Model):
    catagory=models.ForeignKey(catagory,on_delete=CASCADE)
    book_title=models.CharField(max_length=100)    
     