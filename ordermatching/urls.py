from django.urls import path, include
from . import views

appname = 'ordermatching'
urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signupView, name="signup"),
    path("signin/", views.signinView, name="signin"),

]