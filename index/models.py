from django.db import models

# Create your models here.
class Data_user(models.Model):
    firstname=models.CharField(primary_key=True,max_length=15)
    lastname=models.CharField(max_length=255, blank=True, null=True)
    sex=models.CharField(max_length=255, blank=True, null=True)
    email=models.CharField(max_length=255, blank=True, null=True)
    password=models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table='users'