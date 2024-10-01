from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from webapp.models import Post, Our_WORKS_CATEGORY, PRODUCT_CATEGORY, Our_STYLE_CATEGORY


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Post.objects.all()
    
    
class WorkSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    def items(self):
        return Our_WORKS_CATEGORY.objects.all()
    
    
class ProductSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    def items(self):
        return PRODUCT_CATEGORY.objects.all()
    
    
class StyleSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    def items(self):
        return Our_STYLE_CATEGORY.objects.all()









