from django.db import models
from categories.models import Category

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=40)
    image_link = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name


# 5. Tämä on se tietokantamalli, jota haetaan. ViewSetissä Product.objects.all() käyttää tätä mallia.
#    Tuodaan siis myös Category-malli, joka on määritelty categories/models.py-tiedostossa.
#    categories on itse luotu app, joka sisältää Category-mallin.
#    Lopuksi kohti serializeria, joka muotoilee Product-mallin JSON-muotoon.-->


