from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True , blank=True)
    address = models.TextField(null=True , blank=True)

class Car(models.Model):
    car_name = models.CharField(max_length=60)
    speed = models.IntegerField(default=100)

    def __str__(self):
        return {self.car_name , self.speed}

