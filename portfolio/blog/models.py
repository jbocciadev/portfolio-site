from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# from django_summernote.fields import SummernoteTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    content = CKEditor5Field('Content', config_name='extends')
    articleImage = models.ImageField(null=True, upload_to='images/')
    
def __str__(self):
    return f"Article {self.id}" 