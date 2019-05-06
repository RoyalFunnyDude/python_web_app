from django.urls import path
from . import views

# '' path represents the root of the app
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('coolwebsites/', views.cool_websites, name='coolWebsites'),
    path('nameForm/', views.name_form, name='nameForm'),
    path('greet/', views.greet, name='greet'),
    path('login/', views.login, name='login'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('signUpPage/', views.signUpPage, name='signUpPage'),
    path('signUpResult/', views.signUpResult, name='signUpResult'),
]
