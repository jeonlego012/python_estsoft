from django.db import models

# Create your models here.
class UploadFile(models.Model):
    title = models.CharField(default="제목없음", max_length=50)
    file = models.FileField(null=True)

    def __str__(self):
        return f"제목={self.title}"