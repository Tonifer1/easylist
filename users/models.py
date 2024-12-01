from django.db import models
from django.contrib.auth.hashers import make_password  # Salasanan hash-työkalu

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)  # Pidempi kenttä hashille
    accesslevel_id = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.pk and not self.password.startswith("pbkdf2_sha256$"):  # Vain uusille käyttäjille
            self.password = make_password(self.password)  # Hashataan salasana
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

