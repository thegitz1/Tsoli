from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    titre = forms.CharField(label='',
              widget=forms.TextInput(attrs={"placeholder":"Votre Titre"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                'cols': 120
            }
        )
    )
    prix = forms.DecimalField(initial=199.99)

    class Meta:
        model = Produit
        fields = {
            'titre',
            'description',
            'prix'
        }
    def clean_title(self, *args, **kwargs):
        titre = self.cleaned_data.get("titre")
        if not "CFE" in titre:
            return titre
        else:
            raise forms.ValidationError("Ceci n'est pas un titre valide")


class RawProduitForm(forms.Form):
    titre = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Votre Titre"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    prix = forms.DecimalField(initial=199.99)