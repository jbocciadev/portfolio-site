from django.db import models
# from django_summernote.fields import SummernoteTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    content = models.TextField(null=False, blank=True, default="")
    # content = SummernoteTextField(null=True)

def __str__(self):
    return f"Article {self.id}" 