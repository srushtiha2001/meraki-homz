from django.urls import path
from . import views


app_name = 'webapp'




urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),

    path('our_work', views.our_work, name='our_work'),
    path('<int:id>', views.our_work_detail, name='our_work_detail'),

    path('product', views.product, name='product'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),

    path('style', views.style, name='style'),
    path('style_detail/<int:id>', views.style_detail, name='style_detail'),


    path('post_list', views.post_list, name='post_list'),
    path('post_detail/<int:id>', views.post_detail, name='post_detail'),


    path('contact', views.contact, name='contact'),
    path('send_success', views.send_success, name='send_success'),

    
]
