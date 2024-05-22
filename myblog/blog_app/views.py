from django.shortcuts import render, HttpResponseRedirect
from blog_app.forms import SignUpForm

# Create your views here.

#home
def home(request):
    return render(request, 'blog/home.html')

#about
def about(request):
    return render(request, 'blog/about.html')

#contact
def contact(request):
    return render(request, 'blog/contact.html')

#dashboard
def dashboard(request):
    return render(request, 'blog/dashboard.html')

#logout
def user_logout(request):
    return HttpResponseRedirect('/')

#signup
def user_signup(request):
    form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

#login
def login(request):
    return render(request, 'blog/login.html')

