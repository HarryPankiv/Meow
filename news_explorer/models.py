from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    url_to_image = models.URLField(max_length=200)
    publish_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_all_articles():
        return Article.objects.all()