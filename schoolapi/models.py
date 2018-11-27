from django.db import models

# Create your models here.
class Parent (models.Model):
    name=models.CharField(max_length=50)
    #user_id=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name
class Student(models.Model):
    name=models.CharField(max_length=50)
    #user_id=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15,blank=True,null=True)
    parent=models.ManyToManyField('Parent')


    def __str__(self):
        return self.name