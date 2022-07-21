from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.template.loader import render_to_string
from django.views import View

import datetime

from django.conf import settings

from generaltech.models import Author, Tag
from .api_driver.db import Articles


class IndexPageView(View):
    def get(self, request):
        context = getBaseContext()
        main_article, featured_articles, articles, tags =  Articles().getIndexPageArticles()
        context['posts'] = articles
        context['featured_posts'] = featured_articles
        context['main_article'] = main_article
        context['tags'] = tags[:10]
        return render(request, 'generaltech/index.html', context)


class ArticlePageView(View):
    def get(self, request, article_url):
        article = Articles().getArticleContent(article_url)
        context = getBaseContext()
        context['article'] = article
        context['tags'] = context['article'].tags.all()
        context['suggestions'] = Articles().getSuggestedArticles(article_url)
        context['url'] = f'{settings.WEBSITE_ADDR}/article/{article.uri}'
        return render(request, 'generaltech/article.html', context)


class DraftPageView(View):
    def get(self, request, article_uuid):
        context = getBaseContext()
        article = Articles().getDraftContent(article_uuid)
        context['article'] = article
        return render(request, 'generaltech/article.html', context)


class AuthorPageView(View):
    def get(self, request, author_id):
        context = getBaseContext()
        author = Author.objects.get(username=author_id)
        articles = Articles().getAuthorArticlesAndDetails(author_id)
        context['author'] = author
        context['posts'] = articles
        return render(request, 'generaltech/author.html', context)


class TagPageView(View):
    def get(self, request, tag_id):
        context = getBaseContext()
        articles = Articles().getTagArticlesAndDetails(tag_id)
        context['tag'] = Tag.objects.get(slug=tag_id)
        context['posts'] = articles
        return render(request, 'generaltech/tag.html', context)


def getBaseContext():
    return {
        'date': datetime.datetime.now().strftime("%A, %d %b %Y"),
        'facebook_link': f'https://www.facebook.com/{settings.FACEBOOK_ACC}',
        'twitter_link': f'https://twitter.com/{settings.TWITTER_ACC}',
    }
