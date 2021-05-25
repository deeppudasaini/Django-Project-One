from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)      

    def __str__(self):
        return self.firstname;