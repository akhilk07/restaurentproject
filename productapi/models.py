from django.db import models

# Create your models here.


class Products(models.Model):
    product_name=models.CharField(max_length=120)
    category=models.CharField(max_length=120)
    price=models.IntegerField()
    rating=models.FloatField()
    def __str__(self):
        return self.product_name

    # orm query
    # Modelname.objects.create(model_fieldname=value,models_fieldname2=value2,,,,)

    # Products.objects.create(product_name="samsung a52",category="phone",price=32000,rating=4)