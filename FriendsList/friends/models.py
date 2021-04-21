from django.db import models
from phone_field import PhoneField

class Category(models.Model):
    counter = models.PositiveIntegerField(help_text = "counts number of category", unique=True)
    name = models.CharField(max_length = 264, unique = True)

    def __str__(self):
        return self.name

class Info(models.Model):
    counter = models.PositiveIntegerField(help_text = "counts number of category", unique=True)
    category = models.ForeignKey(Category, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length = 50)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email_id = models.EmailField(unique=True, max_length = 50)
    facebook_link = models.URLField(unique=True)

    def __str__(self):
        return self.name
