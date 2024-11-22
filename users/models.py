from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    accesslevel_id = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
