from django.db import models
from django.db.models.base import Model

class category(models.Model):
    category_name=models.CharField(max_length=200,primary_key=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.category_name


class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=200,default="")
    category=models.ForeignKey(category,default="",verbose_name='catogories',on_delete=models.SET_DEFAULT)
    sub_category=models.CharField(max_length=200,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=200,default="")
    pub_date=models.DateField()
    product_quantity=models.IntegerField(default=0)
    product_image=models.ImageField('shop/media')

    def __str__(self):
        return self.product_name