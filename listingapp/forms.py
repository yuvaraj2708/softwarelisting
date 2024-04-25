# forms.py
from django import forms
from .models import Category, Subcategory, SoftwareList

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name']

class SoftwarelistForm(forms.ModelForm):
    class Meta:
        model = SoftwareList
        fields = '__all__'