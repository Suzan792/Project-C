from django import forms
from .models import Design, Product
from art.models import Artwork
from users.models import User


class CreateProductDesignForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(),empty_label="Choose the product you want to add and click the Add Product button below")
    def ArtistSave(self, art_pk,product_pk):
        art = Artwork.objects.get(pk=art_pk)
        product = Product.objects.get(pk=product_pk)
        design = Design.objects.create(art=art,product=product)
        design.save()
    def UserSave(self, art_pk,product_pk,user_pk):
        art = Artwork.objects.get(pk=art_pk)
        product = Product.objects.get(pk=product_pk)
        user = User.objects.get(id=user_pk)
        design = Design.objects.create(art=art,product=product,user=user.userprofile)
        design.save()
