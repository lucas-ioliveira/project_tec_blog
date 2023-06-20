from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Para validar o email
from django.core.validators import validate_email

# Para validar
from django.contrib.auth.models import User

# Para
from django.contrib.auth.decorators import login_required

# Importação do meu model contatos para o formulário no meu dash
from .models import FormContato


# Login
def login(request):
    # Validando o formulário caso não tenha sido postado nada.
    if request.method != "POST":
        messages.info(request, "Nada postato!")
        return render(request, "accounts/login.html")

    # Coletando os dados
    usuario = request.POST.get("usuario")
    senha = request.POST.get("senha")

    # Checando
    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request, "Usuário ou senha invalido!")
        return render(request, "accounts/login.html")
    else:
        auth.login(request, user)
        messages.success(request, "Login realizado com sucasso!")
        return redirect("dashboard")


def logout(request):
    auth.logout(request)
    return redirect("login")


# Cadastro
def cadastro(request):
    # Validando o formulário caso não tenha sido postado nada.
    if request.method != "POST":
        messages.info(request, "Nada postato!")
        return render(request, "accounts/cadastro.html")

    # Coletando os dados do formulário..
    nome = request.POST.get("nome")
    sobrenome = request.POST.get("sobrenome")
    email = request.POST.get("email")
    usuario = request.POST.get("usuario")
    senha = request.POST.get("senha")
    senha2 = request.POST.get("senha2")

    # Verificando se os campos estão preenchidos.
    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, "Nenhum campo pode ficar vazio.")
        return render(request, "accounts/cadastro.html")

    # Validando o e-mail
    try:
        validate_email(email)
    except:
        messages.error(request, "E-mail inválido!")
        return render(request, "accounts/cadastro.html")
    # Checando quse já existe usuário no db.
    if User.objects.filter(email=email).exists():
        messages.error(request, "E-mail já existe!")
        return render(request, "accounts/cadastro.html")

    # Checando quantidades de caracteres da senha.
    if len(senha) < 6:
        messages.error(request, "Senha precisa ter no mínimo 6 caracteres!")
        return render(request, "accounts/cadastro.html")
    if senha != senha2:
        messages.error(request, "Senhas não conferem!")
        return render(request, "accounts/cadastro.html")

    # Checando quantidades de caracters do usuário.
    if len(usuario) < 6:
        messages.error(request, "Usuário precisa ter no mínimo 6 caracteres!")
        return render(request, "accounts/cadastro.html")
    # Checando quse já existe usuário no db.
    if User.objects.filter(username=usuario).exists():
        messages.error(request, "Usuário já existe!")
        return render(request, "accounts/cadastro.html")

    messages.success(request, "Cadastrado com sucesso! Realizar o login.")

    # Inserindo no banco de dados
    user = User.objects.create_user(
        username=usuario,
        email=email,
        password=senha,
        first_name=nome,
        last_name=sobrenome,
    )
    user.save()
    return redirect("login")


# Dashboard
# Para redirecionar se não estiver logado
@login_required(redirect_field_name="login")
def dashboard(request):
    # Validando o formulário caso não tenha sido postado nada.
    if request.method != "POST":
        form = FormContato()
        return render(request, "accounts/dashboard.html", {"form": form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, "Erro ao enviar formulário!")
        form = FormContato(request.POST)
        return render(request, "accounts/dashboard.html", {"form": form})

    form.save()
    return redirect("dashboard")
