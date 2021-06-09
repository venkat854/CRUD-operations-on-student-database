from django.db import models
 
# Create your models here.
 
 
 
class StudentInfo(models.Model):
    name  = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
 
     
 
    class Meta:
        verbose_name = ("StudentInfo")
        verbose_name_plural = ("StudentInfo")
 
    def __str__(self):
        return self.name
