from django.forms import ModelForm, FileField
from .models import UploadFile

class FileUploadForm(ModelForm):
    
    class Meta:
        model = UploadFile
        fields = ("title", "file")

        title = FileField(required=False)

