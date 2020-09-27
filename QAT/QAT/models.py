from django.db import models
class Registration(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    date_of_birth=models.CharField(max_length=10)
    gender=models.CharField(max_length=30)

    def __str__(self):
        return self.username