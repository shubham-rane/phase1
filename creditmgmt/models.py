from django.db import models

class Usercredits(models.Model):
    name=models.CharField(max_length=100)
    credits=models.IntegerField()
    
		