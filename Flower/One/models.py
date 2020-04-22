from django.db import models

# Create your models here.

class Apps(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    KeyApi = models.CharField(max_length=255)
    Des = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name