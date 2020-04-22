from django.db import models

# Create your models here.

class APPModels(models.Model):
    ID = models.IntegerField(primary_key=True, )
    Name = models.CharField(max_length=255)
    KeyApi = models.CharField(max_length=255)

    def __str__(self):
        return self.Name