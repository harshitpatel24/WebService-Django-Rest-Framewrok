from django.db import models

# Create your models here.

class sanlp(models.Model):
    p_id=models.CharField(max_length=50)
    p_name=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.p_name

