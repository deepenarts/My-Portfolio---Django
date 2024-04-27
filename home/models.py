from django.db import models
from django.utils import timezone

class Form(models.Model):
    name= models.CharField(max_length=100,null=False)
    phone= models.CharField(max_length=15)
    email= models.EmailField()
    message= models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.name} - {self.message}"