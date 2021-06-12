from django.forms import ModelForm
from .models import Pic


class URLPicForm(ModelForm):
    class Meta:
        model = Pic
        fields = ['url']


class SizeForm(ModelForm):
    class Meta:
        model = Pic
        fields = ['width', 'height']