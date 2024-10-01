from django.shortcuts import render , redirect
from .models import Testimonials ,Client, Team,  Post, Category , Comment , Our_WORKS_CATEGORY , WorkItem , Our_STYLE_CATEGORY , StyleItem , Product , PRODUCT_CATEGORY , ContactDetails
from .forms import CommentForm , ContactForm
from django.core.paginator import Paginator
from django.core.mail import send_mail as sm 
from django.core.mail import BadHeaderError
from django.http import HttpResponse




# Create your views here.

def home(request):

    testimonials = Testimonials.objects.all()
    post_list = Post.objects.all()
    work_list = Our_WORKS_CATEGORY.objects.all()
    team_list = Team.objects.all()
    product_list = PRODUCT_CATEGORY.objects.all()
    client_list = Client.objects.all()

    

   
    context = {'testimonials': testimonials , 'post_list' : post_list , 'work_list':work_list , 
                'team_list':team_list, 'product_list':product_list,'client_list' : client_list,
               'meta_title': 'Combine Design Bengaluru | Home',
               'meta_description': 'Welcome to Combine Design Bengaluru. Explore our innovative interior design solutions.'
               }
    return render(request, 'webapp/index.html', context)




def about(request):
    
    post_list = Post.objects.all()
    team_list = Team.objects.all()
    testimonials = Testimonials.objects.all()
    product_list = PRODUCT_CATEGORY.objects.all()
    client_list = Client.objects.all()

    context = {'meta_title': 'About Combine Design | Transforming Spaces', 'product_list':product_list,
                'post_list' : post_list ,'team_list':team_list, 'testimonials' : testimonials , 'client_list' : client_list,
               'meta_description': 'Transforming spaces with personalized designs in Bengaluru. Discover inspired living with Combine Design.'
               }

    
    return render(request, 'webapp/about.html' , context)



def our_work(request):
    work_list = Our_WORKS_CATEGORY.objects.all()
    post_list = Post.objects.all()
    testimonials = Testimonials.objects.all()
   
   

    
    
    context = {

		'work_list': work_list ,'post_list' : post_list ,'testimonials': testimonials ,
        'meta_title': '100+ Designs for Your Interiors | 2&3 BHK Interiors ',
        'meta_description': 'Explore our portfolio, which showcases exceptional interior designs crafted by Combine Design. Let our creations inspire your imagination.'


	}

    return render(request, 'webapp/our_work.html', context)



def our_work_detail(request, id):
    our_work_detail = Our_WORKS_CATEGORY.objects.get(id=id)
    our_work_images = WorkItem.objects.filter(category=our_work_detail)
    post_list = Post.objects.all()
    testimonials = Testimonials.objects.all()
    
    
    context = {
        'our_work_detail': our_work_detail , 'our_work_images':our_work_images ,'post_list' : post_list ,'testimonials': testimonials ,
        'meta_title':our_work_detail.meta_title, 
        'meta_description': our_work_detail.meta_description
    }
    return render(request, 'webapp/our_work_detail.html', context)


def product(request):
    product_list = PRODUCT_CATEGORY.objects.all()

    
    context = {

		'product_list': product_list, 
        'meta_title': 'Curated Elegance for Every Space | Combine Design',
        'meta_description': 'Immerse yourself in curated elegance with Combine Designs exclusive range of interior products. Transform your space with sophistication.',
        
        
        


	}

    return render(request, 'webapp/products.html', context)


def product_detail(request , id):
    product_detail = PRODUCT_CATEGORY.objects.get(id=id)
    product_list = Product.objects.filter(category=product_detail)
    testimonials = Testimonials.objects.all()
    

    context = {
        'product_detail': product_detail , 'product_list':product_list ,'testimonials': testimonials ,
        'meta_title':product_detail.meta_title, 
        'meta_description': product_detail.meta_description,

    }
    return render(request, 'webapp/product_detail.html', context)





def style(request):
    style_list = Our_STYLE_CATEGORY.objects.all()
   
    
    
    context = {

		'style_list': style_list , 
        'meta_title': 'From Minimalistic to Contemporary- We Got You Covered',
        'meta_description': 'Dive into a world of diverse interior design styles at Combine Design. From modern to classic, find the perfect aesthetic for your space.'
        


	}

    return render(request, 'webapp/style.html', context)




def style_detail(request , id):
    our_style_detail = Our_STYLE_CATEGORY.objects.get(id=id)
    our_style_images = StyleItem.objects.filter(category=our_style_detail)


    context = {
        'our_style_detail': our_style_detail , 'our_style_images':our_style_images ,
        'meta_title':our_style_detail.meta_title, 
        'meta_description': our_style_detail.meta_description
    }
    return render(request, 'webapp/style_detail.html', context)


def post_list(request):
    post_list = Post.objects.all()
    testimonials = Testimonials.objects.all()



    context = {
        'post_list': post_list,'testimonials': testimonials ,
 'meta_title': 'Stay Updated - Tips from Combine Design’s Experts',
   'meta_description': 'Welcome to Combine Design Bengaluru. Explore our innovative interior design solutions.'
    }

    return render(request, 'webapp/post_list.html', context)




def post_detail(request, id):
    testimonials = Testimonials.objects.all()
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(post=post_detail)
    

    if request.method =='POST' :
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_detail
            new_comment.save()

    else:
        comment_form = CommentForm()





    context = {
		'post_detail':post_detail , 'testimonials': testimonials ,'categories' : categories , 'comments': comments , 
'comment_form':comment_form ,  'meta_title': 'Combine Design Bengaluru | Home',
   'meta_description': 'Welcome to Combine Design Bengaluru. Explore our innovative interior design solutions.'

	}

    return render(request , 'webapp/post_detail.html', context)

def contact(request):

    contactdetails = ContactDetails.objects.last()
    template = 'Webapp/contact.html'

    if request.method == 'POST' : 
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']

            try : 
                sm(subject , message ,from_email , ['merakihomes2022@gmail.com'] )
            
            except BadHeaderError : 
                return HttpResponse('ivalid header')

            return redirect('webapp:send_success')

    else:
        contact_form = ContactForm()


    context = {
        'contactdetails' : contactdetails  , 
        'contact_form' : contact_form
    }


    return render(request, template , context)


def send_success(request):
    return render(request, 'webapp/success.html')

     