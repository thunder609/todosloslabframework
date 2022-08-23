import email
from tkinter import CASCADE
from django.db import models
from datetime import date

# Create your models here.
class Report(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()  

    def __str__(self):
        return  email

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    reporter = models.ForeignKey(Report,on_delete=models.CASCADE)
     
 
    def __str__(self):
         return self.headline
 

        


   
