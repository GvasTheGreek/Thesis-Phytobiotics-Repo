from django import forms

from .models import FilesModel


class UploadFilesForm(forms.ModelForm):
    class Meta:
        model = FilesModel
        fields = ('Index_Name', 'files',)