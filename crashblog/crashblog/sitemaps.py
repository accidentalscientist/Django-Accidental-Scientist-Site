from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Category, Post

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()

class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)
    
    def lastmod(self, obj):
        return obj.created_at

    '''def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return reverse('blog:post_detail', args=[obj.slug])'''