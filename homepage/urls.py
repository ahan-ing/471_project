from django.contrib import admin
from django.urls import path
from . import views
from .views import search_tour_packages


urlpatterns = [
    path('', views.index, name="homepage"),
    path('login',views.loginpg,name='login'),
    path('register',views.register,name='register'),
    path('about', views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('homepage',views.index,name='homepage'),
    path('logout',views.logoutpg,name='logout'),
    
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    
    
    path('guide/register', views.guide_register, name = 'guide_register'),


    path('book-now', views.book_now, name='book_now'),
    path('confirmation.html', views.confirmation_view, name='confirmation'),

    

    path('', search_tour_packages, name='homepage'),
    path('package/search/', search_tour_packages, name='search_tour_packages'),


    path('search/', views.search, name='search'), 
    path('place/<int:id>/', views.place_details, name='place_details'),
    path('division/<int:id>/', views.divison_details, name='division_details'),
    path('package_details/<int:id>/', views.package_details, name='package_details'),
    path('add_package/', views.add_package, name = 'add_package'),
    path('book_package/<int:id>', views.book_package, name = 'book_package'),
    path('guides/', views.guides_list, name='guides_list'),
    path('guides/<int:id>', views.delete_guide, name='delete_guide'),
    path("blog/", views.blog, name='blog'),
    path("blog/play/<int:id>", views.play_blog, name='play_blog'),
    path("add/blog/", views.add_blog, name="add_blog"),
    path("review/<int:id>", views.review, name="review"),
    path("add/review/<int:id>", views.add_review, name = "add_review"),
    path("approve/blogs/", views.approve_blog, name = "approve_blogs"),
    path("approved/blogs/<int:id>", views.approved_blog, name = "approved_blogs")


]




