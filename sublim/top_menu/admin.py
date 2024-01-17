from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from top_menu import models



admin.site.register(models.Main, MPTTModelAdmin)
mptt_indent_field = 50