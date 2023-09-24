from django.contrib import admin
from .models import RegisterModels,TokenModels,StorageModels

admin.site.register(RegisterModels)
admin.site.register(TokenModels)
admin.site.register(StorageModels)

# Register your models here.
