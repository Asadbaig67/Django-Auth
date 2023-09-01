from django.db import models

# Create your models here.


class Custom_User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.username
