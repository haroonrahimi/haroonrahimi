from django import forms
from .models import Category, Info

class CreateNewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CreateNewFriend(forms.ModelForm):
    class Meta():
        model = Info
        fields = '__all__'
