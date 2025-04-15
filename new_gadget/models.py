from django.db import models
import os


# Create your models here.
def image_add(instance, file_name):
    return os.path.join('new_gadget/media', instance.model, file_name)

class Gadget_table(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=image_add)
    price = models.IntegerField()
    about = models.CharField(max_length=2000)

def __str__(self):
    return f"{self.model}"