from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={"placeholder": "Your Title"
                                       }))

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={
                                      "class": "new-class-name two",
                                      "placeholder": "Your description"
                                  }))
    price = forms.DecimalField(initial=1.99)
