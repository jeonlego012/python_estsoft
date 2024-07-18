from django.contrib import admin

# Register your models here.
from .views import User
admin.site.register(User)