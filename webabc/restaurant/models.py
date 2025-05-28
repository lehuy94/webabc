from django.db import models

# Create your models here.
class city(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class menu(models.Model):
    menu = models.TextField(500)   

    def __str__(self):
        return self.menu