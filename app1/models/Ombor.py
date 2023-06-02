from django.db import models



class Omborlar(models.Model):
    nomi = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    employee = models.CharField(max_length=120)
    product = models.CharField(max_length=120)


    def __str__(self):
        return self.nomi


