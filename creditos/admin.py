from django.contrib import admin
from .models import Person, DetailsPerson, DetailsEconomicActivity
# Register your models here.

admin.site.register(Person)
admin.site.register(DetailsPerson)
admin.site.register(DetailsEconomicActivity)