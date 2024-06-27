from django.shortcuts import render

def index_view(request):
    return render(request, 'myapp/index.html')

#def news_view(request):
#   return render(request, 'news/news.html')

def about_view(request):
    return render(request, 'myapp/about.html')

def contact_view(request):
    return render(request, 'myapp/contact.html')

def services_view(request):
    return render(request, 'myapp/services.html')

def blog_view(request):
    return render(request, 'myapp/blog.html')
