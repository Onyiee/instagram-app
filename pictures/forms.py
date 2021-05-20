from django import forms
from .models import photo


class NewPhoto(forms.ModelForm):
    class Meta:
        model = photo
        fields = "__all__"
