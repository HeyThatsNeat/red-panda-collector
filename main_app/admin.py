from django.contrib import admin
# import your models here
from .models import RedPanda, Feeding, Toy

# Register your models here
admin.site.register(RedPanda)
admin.site.register(Feeding)
admin.site.register(Toy)