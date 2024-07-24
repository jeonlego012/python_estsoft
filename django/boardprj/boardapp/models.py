from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    view_count = models.IntegerField(default=0)
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(null=True)
    
    class Meta:
        # UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list
        # : <class 'boardapp.models.Board'> QuerySet.
        # 위 warning 제거
        ordering = ['-pk']

    def __str__(self):
        return f'title={self.title}, author={self.author}, created_at={self.created_at}'