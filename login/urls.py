from django.urls import path, include
from . import views

appname = 'login'
urlpatterns = [
    path("", views.index, name="index"),
    path('trade/',views.tradeView,name='trade'),
    path("signin/", views.signinView, name="signin"),
    path("signup/", views.signupView, name="signup_url"),
]