from django.shortcuts import render, redirect
from ordermatching.models import UserSignup


def home(request):
	return render(request, "home/home.html", {})



def signinView(request):
    
    if request.method == 'POST':
        user_name = request.POST['username']
        pwd = request.POST['password']

        user_obj = UserSignup.objects.filter(username = user_name, password=pwd).exists()
        if user_obj :
            return render(request,"tradelist/accepted/accepted.html",{})
        else :
            return redirect('signup/signup.html') 



def signupView(request):

    if request.method == "POST":
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pwd = request.POST['password']

        if UserSignup.objects.filter(username=user_name).exists():
            print("Username Taken") # use toolkit to show it there(js, css etc)

        user1 = UserSignup.objects.create(username = user_name,firstname=first_name,lastname=last_name,password=pwd)
        user1.save()

        return redirect('home.html')
    else :
        print(request.method)
        return redirect('/')
