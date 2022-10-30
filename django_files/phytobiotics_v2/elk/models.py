from django.db import models
from .validators import validate_file_extension

# Create your models here.


class FilesModel(models.Model):
 
    Index_Name = models.CharField(max_length = 80)
    files = models.FileField(upload_to='files/',validators=[validate_file_extension])
 
    class Meta:
        ordering = ['Index_Name']
     
    def __str__(self):
        return f"{self.Index_Name}"