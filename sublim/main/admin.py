from django.contrib import admin
from .models import Good, Kategory
#               ЗАКОМЕНЧЕНА СТАРАЯ ФУНКЦИЯ ЧТОБ ЗА НЕЁ РАБОТАЛИ ДРУГИЕ ПАРАМЕТРЫ
# class GoodAdmin(admin.ModelAdmin):
#    list_display = [
#        field.name for field in Good._meta.fields if field.name != "id"]

class GoodAdmin(admin.ModelAdmin):
    list_display = ('picture', 'namegood', 'content', 'specification', 'price')
    list_display_links = ('picture', 'namegood')

class KategoryAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Kategory._meta.fields if field.name != "id"
    ]
admin.site.register(Kategory, KategoryAdmin)
admin.site.register(Good, GoodAdmin)