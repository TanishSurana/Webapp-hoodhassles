from django.contrib import admin
from .models import Complain

# register your models here.

class Complainadmin(admin.ModelAdmin):
    filter_horizontal = ("voters",)

admin.site.register(Complain, Complainadmin)

