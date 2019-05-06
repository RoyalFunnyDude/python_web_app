from django.db import models

# Create your models here.


class Person(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.lastName + ', ' + self.firstName


class LoginCredential(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    userName = models.CharField(max_length=10)
    passWord = models.CharField(max_length=10)

    def __str__(self):
        password_display = ''
        for each in range(len(self.passWord)):
            password_display += '*'
        return 'Username: ' + self.userName + ' | Password: ' + password_display
