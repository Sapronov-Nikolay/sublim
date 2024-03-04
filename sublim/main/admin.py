from django.contrib import admin
from .models import Good, Category, Cart
#               ЗАКОМЕНЧЕНА СТАРАЯ ФУНКЦИЯ ЧТОБ ЗА НЕЁ РАБОТАЛИ ДРУГИЕ ПАРАМЕТРЫ
# class GoodAdmin(admin.ModelAdmin):
#    list_display = [
#        field.name for field in Good._meta.fields if field.name != "id"]

@admin.register(Good) # Задекорировано согласно учебному пособию для прописания слага
class GoodAdmin(admin.ModelAdmin):
    list_display = ('picture', 'namegood', 'content', 'specification', 'price', 'quatity', 'category') # Отображает поля в админке
    list_display_links = ('picture', 'namegood', 'quatity', 'category')  # Даёт кликать по ним для редактирования
    prepopulated_fields = {'slug': ('namegood',)} # Автоматическое добавление слага


@admin.register(Category) # Задекорировано согласно учебному пособию для прописания слага
class CategoryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('categoriya',)} # Автоматическое добавление слага

# -----------ОСТАВЛЕНО НА ВСЯКИЙ СЛУЧАЙ ДЛЯ ИНФОРМАЦИИ------------
    #list_display = [
    #    field.name for field in Category._meta.fields if field.name != "id"
    #]

@admin.register(Cart) # Задекорировано согласно учебному пособию для прописания слага
class CartAdmin(admin.ModelAdmin):
    list_display = ('picture', 'namegood', 'price') # Отображает поля в админке
    prepopulated_fields = {'slug': ('namegood',)} # Автоматическое добавление слага


# -----------ЗАКОМЕНТИРОВАНО ИЗ-ЗА ДЕКОРИРОВАНИЯ------------
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Good, GoodAdmin)
#admin.site.register(Cart, CartAdmin)