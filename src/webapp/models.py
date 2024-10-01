from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimonials')
    content = models.TextField()





    
    def __str__(self):
        return self.name
    

class Client(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimonials')
    





    
    def __str__(self):
        return self.name
    


class Team(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimonials')
    designation = models.CharField(max_length=1000, null=True , blank = True)
    facebook_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)






    
    def __str__(self):
        return self.name



#------------------------------------------------- Blog Section -------------------------------------------------#


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    title1 = models.CharField(max_length=1000, null=True, blank=True)
    content1 = models.TextField()
    title2 = models.CharField(max_length=1000, null=True, blank=True)
    content2 = models.TextField()
    title3 = models.CharField(max_length=100 , null=True, blank=True)
    content3 = models.TextField()
    title4 = models.CharField(max_length=100 , null=True, blank=True)
    content4 = models.TextField()
    title5 = models.CharField(max_length=100 , null=True, blank=True)
    content5 = models.TextField()

     
    meta_title = models.CharField(max_length=1000 , null=True , blank=True)
    meta_description = models.CharField(max_length=1000 , null=True , blank=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True,  on_delete=models.SET_NULL)
    created = models.DateTimeField(default=timezone.now)
    
    
    
    
    def __str__(self):
        return self.title




class Category(models.Model):
	category_name = models.CharField(max_length=50)



	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'


	def __str__(self):
		return self.category_name



class Comment(models.Model):
	User = models.ForeignKey(User , on_delete=models.CASCADE)
	post = models.ForeignKey(Post , on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(default=timezone.now)



#------------------------------------------------- Blog Section End-------------------------------------------------#



#------------------------------------------------- Our Work Section Starts-------------------------------------------------#



class Our_WORKS_CATEGORY(models.Model):
    category_name = models.CharField(max_length=1000 , null=True , blank=True)
    category_image = models.ImageField(upload_to='Our_Works' , null=True , blank=True)
    meta_title = models.CharField(max_length=1000 ,null=True ,blank=True)
    meta_description = models.TextField(null=True , blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
	


class WorkItem(models.Model):
    category = models.ForeignKey(Our_WORKS_CATEGORY, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Our_Works' , null=True , blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.category_name
    
#------------------------------------------------- Our Work Section Ends-------------------------------------------------#

#------------------------------------------------- Style  Starts-------------------------------------------------#

    

class Our_STYLE_CATEGORY(models.Model):
    category_name = models.CharField(max_length=1000 , null=True , blank=True)
    category_image = models.ImageField(upload_to='Our_Works' , null=True , blank=True)
    category_desription = models.TextField(null=True , blank=True)
    meta_title = models.CharField(max_length=1000 ,null=True ,blank=True)
    meta_description = models.TextField(null=True , blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
	


class StyleItem(models.Model):
    category = models.ForeignKey(Our_STYLE_CATEGORY, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Our_Works' , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.category_name
    
	
#------------------------------------------------- Style Ends-------------------------------------------------#


#------------------------------------------------- Product  Starts-------------------------------------------------#

    

class PRODUCT_CATEGORY(models.Model):
    category_name = models.CharField(max_length=1000 , null=True , blank=True)
    image = models.ImageField(upload_to='Our_Works' , null=True , blank=True)
    description = models.TextField(null=True ,blank=True)
    meta_title = models.CharField(max_length=1000 ,null=True ,blank=True)
    meta_description = models.TextField(null=True , blank=True)



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
	


class Product(models.Model):
    product_name = models.CharField(max_length=1000 , null=True , blank=True)
    category = models.ForeignKey(PRODUCT_CATEGORY, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Our_Works' , null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
	
#------------------------------------------------- Product Ends-------------------------------------------------#

class ContactDetails(models.Model):
    # location = 
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return str(self.id)