from django.contrib import admin


# Register your models here.
from .models import *

admin.site.register(Flyer_Image)
admin.site.register(Flyer)
admin.site.register(Reminder)