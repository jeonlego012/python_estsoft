from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=False)
    explain = models.TextField()
    
    def __str__(self):
        return f'Member[id={self.id}, name={self.name}, age={self.age}, explain={self.explain}]'
    
class Log(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    regdate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Log[id={self.id}, title={self.name},...]'

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Person[id={self.id}, first_name={self.first_name}, last_name={self.last_name}]'