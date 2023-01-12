from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class Breed(models.Model):
    breed = models.CharField(max_length=50)

    def __str__(self):
        return self.breed

class Pet(models.Model):
    choices_status = (('P', 'Para adoção'),
                      ('A', 'Adotado'))

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='photos_pets')
    name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default='P')

    def __str__(self):
        return self.name                  