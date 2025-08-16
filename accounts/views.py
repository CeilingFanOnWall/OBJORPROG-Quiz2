from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse

def base(request):
    return render(request, 'accounts/base.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Adjust as needed
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    return render(request, 'accounts/profile.html')

def account_home(request):
    return HttpResponse("Accounts Home Page")