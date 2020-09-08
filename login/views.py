from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def tradeView(request):
    return render(request,'trade.html')

def signinView(request):
    
    if request.method == 'POST':
        user_name = request.POST['username']
        pwd = request.POST['password']

        print(user_name)

        return render(request,'trade.html')
    else :
        print("Not done")
        return render(request,'signin.html')


def signupView(request):
    if request.method == "POST":
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pwd = request.POST['password']

        print(user_name+pwd)
        return render(request,'trade.html')
    else :
        return render(request,'signup.html')


''' 
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
        return render(response, 'signup/signup.html') 




        user_obj = UserSignup.objects.filter(username = user_name, password=pwd).exists()
        if user_obj :
            return render(request,'/tradelist/accepted.html',{})
        else :
            return render(request,'/signup/signup.html')
    else:
        return render(request, 'signin/signin.html')'''

