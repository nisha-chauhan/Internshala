from django.db import models

# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=200)
    user_id=models.CharField(max_length=200)
    phone=models.CharField (max_length=10)
    role=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name