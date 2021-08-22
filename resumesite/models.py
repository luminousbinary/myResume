from django.db import models
# from django.db.models.fields import EmailField

# Create your models here.


class Contact(models.Model):
    name = models.CharField( max_length=50)
    email= models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

