"""lostandfound URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('team/', views.team, name='team-page'),
    path('signin/', views.signin, name='signin-page'),
    path('signup/', views.signup, name='signup-page'),
    path('signout/', views.signout, name='signout'),
    path('home2/', views.home2, name='home-page-2'),
    path('profile/', views.profile, name='profile-page'),
    path('report_lost_person/', views.report_lost_person, name='report-lost-person-page'),
    path('report_found_person/', views.report_found_person, name='report-found-person-page'),
    path('report_lost_object/', views.report_lost_object, name='report-lost-object-page'),
    path('report_found_object/', views.report_found_object, name='report-found-object-page'),
    path('report_lost_pet/', views.report_lost_pet, name='report-lost-pet-page'),
    path('report_found_pet/', views.report_found_pet, name='report-found-pet-page'),
    path('view_lost_pet/', views.view_lost_pet, name='view-lost-pet-page'),
    path('view_found_person/', views.view_found_person, name='view-found-person-page'),
    path('view_found_object/', views.view_found_object, name='view-found-object-page'),
    path('view_lost_person/', views.view_lost_person, name='view-lost-person-page'),
    path('view_lost_object/', views.view_lost_object, name='view-lost-object-page'),
    path('view_found_pet/', views.view_found_pet, name='view-found-pet-page'),
    path('my_lost_person/', views.my_lost_person, name='my-lost-person-page'),
    path('my_lost_object/', views.my_lost_object, name='my-lost-object-page'),
    path('my_lost_pet/', views.my_lost_pet, name='my-lost-pet-page'),
    path('my_found_person/', views.my_found_person, name='my-found-person-page'),
    path('my_found_object/', views.my_found_object, name='my-found-object-page'),
    path('my_found_pet/', views.my_found_pet, name='my-found-pet-page'),
    path('delete_lost_pet/<int:id>', views.delete_lost_pet, name='delete-lost-pet-page'),
    path('delete_lost_person/<int:id>', views.delete_lost_person, name='delete-lost-person-page'),
    path('delete_lost_object/<int:id>', views.delete_lost_object, name='delete-lost-object-page'),
    path('my_found_pet/', views.my_found_pet, name='my-found-pet-page'),
    path('delete_found_pet/<int:id>', views.delete_found_pet, name='delete-found-pet-page'),
    path('delete_found_person/<int:id>', views.delete_found_person, name='delete-found-person-page'),
    path('delete_found_object/<int:id>', views.delete_found_object, name='delete-found-object-page'),
    path('edit_lost_pet/<int:id>', views.edit_lost_pet, name='edit-lost-pet-page'),
    path('edit_lost_object/<int:id>', views.edit_lost_object, name='edit-lost-object-page'),
    path('edit_found_pet/<int:id>', views.edit_found_pet, name='edit-found-pet-page'),
    path('edit_found_object/<int:id>', views.edit_found_object, name='edit-found-object-page'),
    path('edit_lost_person/<int:id>', views.edit_lost_person, name='edit-lost-person-page'),
    path('edit_found_person/<int:id>', views.edit_found_person, name='edit-found-person-page'),
    path('search_lost_pet/', views.search_lost_pet, name='search-lost-pet-page'),
    path('search_found_pet/', views.search_found_pet, name='search-found-pet-page'),
    path('search_lost_object/', views.search_lost_object, name='search-lost-object-page'),
    path('search_found_object/', views.search_found_object, name='search-found-object-page'),
    path('search_lost_person/', views.search_lost_person, name='search-lost-person-page'),
    path('search_found_person/', views.search_found_person, name='search-found-person-page'),

   



    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)