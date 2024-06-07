from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'users/index.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html', {})


def user_login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                return HttpResponse("user authenticated and logged in")
            else:
                return HttpResponse("Invalid credentials")

    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


