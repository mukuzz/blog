from django.contrib import admin
from .models import Article, Tag, Author

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Author)