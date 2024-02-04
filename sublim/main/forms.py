from main import models
from django.forms import ModelForm


class GoodForm(ModelForm):
    class Meta:
        model = models.Good
        fields = [  # генератор-выражение, формирующее список полей нашеё таблицы для отображения в админке
            field.name for field in models.Good._meta.fields if field.name != "id"]
# перебор полей, такой же, как в админке


class SearchForm(ModelForm):
    class Meta:
        # model = models.Good
        fields = ["poisk"]

class CartForm(ModelForm):
    class Meta:
        model = models.Cart
        fields = [field.name for field in models.Cart._meta.fields if field.name != "id"]
