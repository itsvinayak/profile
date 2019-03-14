from .models import msg
from django.forms import ModelForm


class msgForm(ModelForm):
    class Meta:
        model= msg
        fields=['name','email','text']
