from django.contrib import admin

# Register your models here.
from web.models import Shop, Good

admin.site.register(Shop)
admin.site.register(Good)