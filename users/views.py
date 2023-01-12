from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.user.is_authenticated:
        return redirect('/disclose/new_pet')
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        confirm_password = request.POST.get('confirmar_senha')

        if len(name.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 or len(confirm_password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return render(request, 'register.html')

        if password != confirm_password:
            messages.add_message(request, constants.ERROR, 'Preencha duas senhas iguais')
            return render(request, 'register.html')

        try:
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )        
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
            return render(request, 'register.html')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return render(request, 'register.html')

def auth_login(request):
    if request.user.is_authenticated:
        return redirect('/disclose/new_pet')
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        name = request.POST.get('nome')
        password = request.POST.get('senha')  
        user = authenticate(username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return render(request, 'login.html')    

def logout_user(request):
    logout(request)
    return redirect('/auth/login')