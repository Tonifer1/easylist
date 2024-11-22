from django.db import models

from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)
    image_link = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.category_name

