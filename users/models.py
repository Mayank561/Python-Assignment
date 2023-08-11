from django.db import models
# users/models.py
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()
    
    class Meta:
        app_label = 'users'  # Add this line to specify the app label

    def __str__(self):
        return self.first_name
