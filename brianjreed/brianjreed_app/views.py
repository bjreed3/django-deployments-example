from django.shortcuts import render
from brianjreed_app.forms import UserForm,UserProfileInfoForm

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    # context_dict = {'text':'hello world!', 'number':'120'}
    return render(request,'brianjreed_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic'  in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'brianjreed_app/registration.html',
                {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                # Log the user in
                login(request,user)
                # Send the user back to a page
                # in this case their homepage
                return HttpResponseRedirect(reverse('index'))
            else:
                # if account is not active:
                return HttpResponse('Account is not active')
        else:
            print("Failed Login")
            # print("Username: {} and password {}".format(username,password))
            return HttpResponse ("Invalid login supplied")
    else:
        return render(request,'brianjreed_app/login.html')

def aboutme(request):
    return render(request,'brianjreed_app/aboutme.html')

def other(request):
    return render(request,'brianjreed_app/other.html')

def relative(request):
    return render(request,'brianjreed_app/relative_url_templates.html')
