from django.contrib import admin

# Register your models here.
from .models import Testimonials , Client, Team,  Post , Category , Comment , Our_WORKS_CATEGORY , WorkItem ,  Our_STYLE_CATEGORY , StyleItem , PRODUCT_CATEGORY , Product


admin.site.register(Testimonials)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Our_WORKS_CATEGORY)
admin.site.register(WorkItem)
admin.site.register(Our_STYLE_CATEGORY)
admin.site.register(StyleItem)
admin.site.register(PRODUCT_CATEGORY)
admin.site.register(Product)
admin.site.register(Team)
admin.site.register(Client)





