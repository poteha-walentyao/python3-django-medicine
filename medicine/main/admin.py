from django.contrib import admin
from .models import Doctor, Division, Client


admin.site.register(Division)
admin.site.register(Doctor)
admin.site.register(Client)
