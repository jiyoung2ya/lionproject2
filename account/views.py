from django.contrib.auth.password_validation import password_changed
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm #UserCreationForm #로그인폼, 회원가입폼
from django.contrib.auth import authenticate,login, logout, logout
from .forms import RegisterForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None: #유저가 존재할때
                login(request,user)
                
        return redirect("home") #로그인에 실패해도 홈으로 돌아가

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request): #로그인할때 숫자랑 특수기호 여러개 필요
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() #꼭필요한정보가 없기 떄문에 commit없어도 됨????
            login(request,user)
        return redirect("home")      
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form':form}) 