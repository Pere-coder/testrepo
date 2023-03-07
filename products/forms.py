from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField()
        
    class Meta:
        model = Products
        fields =[
            'title',
            'description',
            'price'
        ]
        
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("this is not a valid title")
        return title
        
class RawProductForm(forms.Form):
    title =forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField()
        