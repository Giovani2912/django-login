# PRECISO ARRUMAR AS FUNÇÕES DE CADASTRO E DE LOGIN
# DETALHES NA URL(APARECE A SENHA, SEM CRIPTOGRAFAR)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User  
from django.contrib import auth

# Create your views here.
def index(request):
    return render (request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print("Preencha os campos")
            return redirect('index')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('home')
                
        # essa é a primeria linha a ser digitada dentro da função, com o objetivo de renderizar a tela em chamada
    return render(request, 'login.html')
    
def cadastro(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        nome = request.POST['nome']
        celular = request.POST['tel']
        cpf = request.POST['cpf']

        if User.objects.filter(email=email).exists():
            print('Usuário ja cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        
        
        print('Usuário cadastrado com sucesso')
        return redirect ('login')
    else:
        # essa é a primeria linha a ser digitada dentro da função, com o objetivo de renderizar a tela em chamada
        return render(request, 'cadastro.html')


def home(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return redirect('index')