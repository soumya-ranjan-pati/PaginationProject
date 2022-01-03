from django.db import models

# Create your models here.
class ProductModel(models.Model):
    idno=models.IntegerField(unique=True)
    photo=models.FileField(upload_to="productimagess/")
