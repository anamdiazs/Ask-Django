from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser,AbstractBaseUser

def login_view(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = authenticate()
        if request.method == 'POST':
        
            username = request.POST['username']
            password = request.POST['password']
            print("-----------------")
            print(username,password)
            print("-----------------")
            user = authenticate(username= username, password= password)
            if user is not None:
                    login(request, user)
                    return redirect ('Login')
            else:
                messages.info(request,'Username or password invalid')
                context= {}
                return render(request,'home.html',context)            
        context = {}
        return render(request,'login.html',context)

def registro(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages .success(request,'Account was created for' + user)
                return redirect('Home')
        return render (request, 'registro.html',{'form':form})

@login_required(login_url='Login')

def home(request):
    questions_render = create_question.objects.all()
    categories_render = Categories.objects.all()
    ciencia = Categories.objects.filter(id=1)
    salud = Categories.objects.filter(id=2)
    social = Categories.objects.filter(id=3)
    recetas = Categories.objects.filter(id=4)
    context= {'questions_render':questions_render,
            'categories_render':categories_render,'ciencia':ciencia,'salud':salud,'social':social,'recetas':recetas}
    print("Questions render")
    print(questions_render)
    return render(request, 'home.html',context)

@login_required(login_url='Login')
def logout_view(request):
    logout(request)
    return redirect('Login')

def questions_view(request):  
    return render(request, 'question.html')

@login_required(login_url='Login')
def upload_question(request):
    form = CreateQuestion()
    if request.method == "POST":
        form = CreateQuestion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context ={'form':form}
    return render(request,'question.html',context)

def upload_answer(request,question_id):
    form = CreateAnswer()
    question =create_question.objects.get(id=question_id)
    if request.method == "POST":
        form = CreateAnswer(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    context ={'form':form,'question':question}
    return render(request,'answers.html',context)
            
def show_answers(request):
    answer_render = create_answer.objects.all()
    categories_render = Categories.objects.all()
    form= CreateAnswer()
    if request.method == "POST":
        form = CreateAnswer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form,'answer_render':answer_render, 'categories_render':categories_render}
    return render(request,'show_answer.html',context)    

def get_answers(request, question_id):
    get_answer = create_answer.objects.get(id=question_id)
    context = {'get'}
    return()
    print(get_answer)