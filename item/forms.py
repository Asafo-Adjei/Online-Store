from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border' #setting INPUT_CLASSES as a variable

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs = {           #seleccting the category section and styling it. The "forms.Select" creates a select field similar to using the select tag in html
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs = {           #seleccting the name section and styling it
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs = {           
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs = {           
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs = {           
                'class': INPUT_CLASSES
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold', )

        widgets = {
            'name': forms.TextInput(attrs = {           #seleccting the name section and styling it
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs = {           
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs = {           
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs = {           
                'class': INPUT_CLASSES
            }),
        }
