from django.forms import ModelForm, CharField
from .models import Board

class BoardModelForm(ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'contents')
