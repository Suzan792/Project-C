from django import forms
from .models import Design, Product
from art.models import Artwork


class CreateProductDesignForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    def save(self, art_pk,product_pk):
        art = Artwork.objects.get(pk=art_pk)
        product = Product.objects.get(pk=product_pk)
        design = Design.objects.create(art=art,product=product)
        design.save()
