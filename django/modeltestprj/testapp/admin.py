from django.contrib import admin
from .models import Member, Log, Person

# Register your models here.
admin.site.register(Member)
admin.site.register(Log)
admin.site.register(Person)