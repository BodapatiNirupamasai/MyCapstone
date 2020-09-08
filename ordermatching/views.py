from django.shortcuts import render, redirect
from ordermatching.models import UserSignup
from django.template import loader
from django.http import HttpResponse

def home(request):
	return render(request, "home/home.html", {})

def tradeView(request):
    return render(request,'trade.html')

def signinView(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pwd = request.POST['password']

        user_obj = UserSignup.objects.filter(username = user_name, password=pwd).exists()
        if user_obj :
            print("user object ecists")
            return render(request,'trade.html')
        else :
            return render(request,'/signup/signup.html')
    else:
        return render(request, 'signin/signin.html')



def signupView(request):
    if request.method == "POST":
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pwd = request.POST['password']

        if UserSignup.objects.filter(username=user_name).exists():
            print("Username Taken") # use toolkit to show it there(js, css etc)
        else :
            user1 = UserSignup.objects.create(username = user_name,firstname=first_name,lastname=last_name,password=pwd)
            user1.save()
            print("User Created")
            return render(request,'trade.html')
    else :
        return render(request,'signup/signup.html')

        
'''
def signinView(request):
    
    if request.method == 'POST':
        user_name = request.POST['username']
        pwd = request.POST['password']

        user_obj = UserSignup.objects.filter(username = user_name, password=pwd).exists()
        if user_obj :
            return render(request,'/tradelist/accepted.html',{})
        else :
            return render(request,'/signup/signup.html')
    else:
        return render(request, 'signin/signin.html')


def signupView(response):

    if response.method == "POST":
        user_name = response.POST['username']
        first_name = response.POST['firstname']
        last_name = response.POST['lastname']
        pwd = response.POST['password']

        if UserSignup.objects.filter(username=user_name).exists():
            print("Username Taken") # use toolkit to show it there(js, css etc)
        else :
            user1 = UserSignup.objects.create(username = user_name,firstname=first_name,lastname=last_name,password=pwd)
            user1.save()
            print("User Created")
            return redirect('/')
    else :
        print(response.method)
        return redirect('/')
        print("ok")
        return render(response, 'signup/signup.html') '''