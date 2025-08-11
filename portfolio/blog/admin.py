from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
from .models import Article

# @admin.register(Article)
# class ArticleAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "excerpt"]
    pass

# admin.site.register(Article,)
# Register your models here.
