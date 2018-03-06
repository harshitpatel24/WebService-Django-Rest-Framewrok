from django.db import models

# Create your models here.
from rest_framework.fields import ListField


class sanlp(models.Model):
    p_id=models.CharField(max_length=50)
    p_name=models.CharField(max_length=500)
    review_detail=ListField()


    def __str__(self):
        return self.p_name

