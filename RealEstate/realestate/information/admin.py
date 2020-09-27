from django.contrib import admin
from .models import Buildings, Interior, Agents

# Register your models here.
admin.site.register(Buildings)
admin.site.register(Interior)
admin.site.register(Agents)