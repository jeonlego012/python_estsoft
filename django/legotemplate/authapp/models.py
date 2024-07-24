from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    # password2 = models.CharField(max_length=128, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return f'Model User) username={self.username}, email={self.email}'