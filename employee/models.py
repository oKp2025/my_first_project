from django.db import models

# Create your models here.
class Employee(models.Model):
    FirstName =models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    EmployeeId = models.IntegerField(unique = True)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)

 
 
    def __str__(self):
        return (self.FirstName+self.LastName)