from requests.exceptions import HTTPError
import datetime

from django.conf import settings

from generaltech.models import Article, Tag, Author

class Articles:

    def getIndexPageArticles(self):
        articles = Article.objects.all()
        main_article = articles[0]
        featured_articles = articles[1:3]
        articles = articles
        tags = Tag.objects.all()
        return main_article, featured_articles, articles, tags

    def getArticleContent(self, article_url):
        article = Article.objects.get(uri=article_url)
        return article
    
    def getSuggestedArticles(self, article_url):
        return Article.objects.all()[:3]

    def getDraftContent(self, article_uuid):
        response = self.getContentFromApi(parameters={
            'project': settings.PROJECT_UUID,
            'q_type': 'single',
            'uuid': article_uuid,
            'suggestions': settings.RELATED_ARTICLE_COUNT
        }, published=False, req_type="drafts")
        response_dict = response.json()
        response_dict['created_on'] = self.formatCreationDate(response_dict['created_on'])
        response_dict['suggestions'] = list(map(
            self.formatArticle, response_dict['suggestions']
        ))
        response_dict['url'] = f'{settings.WEBSITE_ADDR}/draft/{response_dict["url"]}'
        response_dict['twitter_acc'] = settings.TWITTER_ACC
        return response_dict

    def getAuthorArticlesAndDetails(self, author_id):
        return Article.objects.all()

    def getTagArticlesAndDetails(self, tag_id):
        return Article.objects.all()


    def formatArticle(self, article):
        article.publish_time = self.formatCreationDate(article.publish_time)
        return article

    def formatCreationDate(self, d):
        if d.date() == datetime.date.today():
            return "Today at " + d.strftime("%I:%M %p")
        elif d.date() == datetime.date.today() - datetime.timedelta(days=1):
            return "Yesterday at " + d.strftime("%I:%M %p")
        else:
            return d.strftime("%b %d, %Y")
