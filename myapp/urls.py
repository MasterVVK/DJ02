from django.urls import path
from . import views
from news import views as news_views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('news/', news_views.news_view, name='news'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('services/', views.services_view, name='services'),
    path('blog/', views.blog_view, name='blog'),
]
