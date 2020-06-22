from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from admin.song.models import Song

# Create your views here.@login_required(login_url = 'user.login')

def register(request):
    return render(request,'userTemplates/signup/index.html')


def signup(request):

    if request.method == 'POST':

        if not 'firstname' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('user.register')

        if not 'lastname' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('user.register')

        if not 'username' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('user.register')

        if not 'email' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('user.register')

        if not 'password1' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('user.register')


        if not 'password2' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('user.register')

        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken')
                return redirect('user.register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect('user.register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('user.login')
        else:
            messages.error(request,'password not matching...')
            return redirect('user.register')
        return redirect('user.register')

    else:
        return redirect('user.register')

def login(request):
    return render(request,'userTemplates/login/index.html')

def login_post(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('user.index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('user.login')
    else:
         return redirect('user.login')


# @login_required(login_url = 'user.login')
def index(request):
        data = Song.objects.order_by('-id')

        return render(request, 'userTemplates/index.html', {'data':data})


@login_required(login_url = 'user.login')
def logout(request):
    auth.logout(request)
    return redirect('user.login')