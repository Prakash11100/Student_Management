from django.db import models

# Create your models here.
class Student_db(models.Model):
    Name=models.CharField(max_length=50)
    Contact=models.IntegerField()
    Mail=models.EmailField()
    