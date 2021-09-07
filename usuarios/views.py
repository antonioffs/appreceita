from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


# Create your views here.

def cadastro(request):
    if(request.method == 'POST'):
        password = request.POST['password']
        password2 = request.POST['password2']
        nome = request.POST['nome']
        email = request.POST['email']
        if(senhas_nao_sao_iguais(password, password2)):
            messages.error(request, 'As senhas são diferentes')
            return redirect('cadastro')
        if(valida_campo_vazio(nome)):
            messages.error(request, "O campo 'nome' não pode ficar em branco")
            return redirect('cadastro')
        if(valida_campo_vazio(email)):
            messages.error(request, "O campo 'email' nao pode ficar em branco")
            return redirect('cadastro')
        if(User.objects.filter(email=email).exists()):
            messages.error(request, 'Email já cadastrado')
            print()
            return redirect('cadastro')
        if(User.objects.filter(username=nome).exists()):
            messages.error(request, 'Nome já cadastrado')
            print()
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()

        messages.success(request, 'Cadastro criado com sucesso')
        return redirect('login')
    return render(request, 'usuarios/cadastro.html')

def login(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        if(valida_campo_vazio(email) or valida_campo_vazio(password)):
            messages.error(request, "Os campos 'Email' e 'Senha' devem ser preechidos")
            return redirect('login')
        
        if(User.objects.filter(email=email).exists()):
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
        
            user = auth.authenticate(request, username=username, password=password)
            if(user is not None):
                auth.login(request, user)
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def dashboard(request):
    if(request.user.is_authenticated):
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas' : receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')
    
def cria_receita(request):
    if(request.method == 'POST'):
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo, 
        tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)

        receita.save()

        return redirect('dashboard')

    else:
        messages.error(request, "O preenchimento de todos os campos são obrigatórios")
        return render(request, 'usuarios/cria_receita.html')

def valida_campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(password1, password2):
    return password1 != password2
