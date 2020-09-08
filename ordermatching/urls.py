from django.urls import path, include
from . import views

appname = 'ordermatching'
urlpatterns = [
    path("", views.home, name="home"),
    path("signin/", views.signinView, name="signin"),
    path('trade/',views.tradeView,name='trade'),
    path("signup/", views.signupView, name="signup_url"),

]