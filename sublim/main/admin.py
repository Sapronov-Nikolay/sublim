from django.contrib import admin
from .models import Good

class GoodAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Good._meta.fields if field.name != "id"]


admin.site.register(Good, GoodAdmin)