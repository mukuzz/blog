from django.shortcuts import render
from django.views import View

import datetime

from django.conf import settings

from generaltech.models import Article, Author, Tag


class IndexPageView(View):
    def get(self, request):
        context = getBaseContext()
        articles = Article.objects.filter(published=True)
        context['posts'] = articles
        context['featured_posts'] = articles[1:3]
        context['main_article'] = articles[0]
        context['tags'] = Tag.objects.all()[:10]
        return render(request, 'generaltech/index.html', context)


class ArticlePageView(View):
    def get(self, request, article_url):
        article = Article.objects.get(uri=article_url, published=True)
        context = getBaseContext()
        context['article'] = article
        context['tags'] = article.tags.all()
        context['suggestions'] = article.related_articles.all()
        context['url'] = f'{settings.WEBSITE_ADDR}/article/{article.uri}'
        return render(request, 'generaltech/article.html', context)


class DraftPageView(View):
    def get(self, request, article_url):
        article = Article.objects.get(uri=article_url, published=False)
        context = getBaseContext()
        context['article'] = article
        context['tags'] = article.tags.all()
        context['suggestions'] = article.related_articles.all()
        context['url'] = f'{settings.WEBSITE_ADDR}/article/{article.uri}'
        return render(request, 'generaltech/article.html', context)


class AuthorPageView(View):
    def get(self, request, author_id):
        context = getBaseContext()
        author = Author.objects.get(username=author_id)
        articles = author.article_set.all()
        context['author'] = author
        context['posts'] = articles
        return render(request, 'generaltech/author.html', context)


class TagPageView(View):
    def get(self, request, tag_id):
        context = getBaseContext()
        tag = Tag.objects.get(slug=tag_id)
        context['tag'] = tag
        context['posts'] = tag.article_set.all()
        return render(request, 'generaltech/tag.html', context)


def getBaseContext():
    return {
        'date': datetime.datetime.now().strftime("%A, %d %b %Y"),
        'facebook_link': f'https://www.facebook.com/{settings.FACEBOOK_ACC}',
        'twitter_link': f'https://twitter.com/{settings.TWITTER_ACC}',
    }
