from django.db import models

# Create your models here.

class product(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image_url=models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
