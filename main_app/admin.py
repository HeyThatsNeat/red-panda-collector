from django.contrib import admin
# import your models here
from .models import RedPanda, Feeding

# Register your models here
admin.site.register(RedPanda)
admin.site.register(Feeding)