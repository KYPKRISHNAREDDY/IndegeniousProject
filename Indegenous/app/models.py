from django.db import models

# Create your models here.


class Element(models.Model):
    Name=models.CharField(max_length=20)
    Text=models.TextField() 

    def __str__(self):
        return str(self.id)