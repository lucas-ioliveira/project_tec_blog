# Importação dos módulos do Django para renderizar meu html e levantamento de erros
from django.shortcuts import render, get_object_or_404, redirect

# Importação levantamento de erros
from django.http import Http404

# Importação do meu módulo de contato
from .models import Posts

# Importação do módulo do Django para paginação
from django.core.paginator import Paginator

# Importação do módulo do Django
from django.contrib import messages

from comentarios.models import Comment


def index(request):
    posts = Posts.objects.order_by("id").filter(post_published=True)
    paginator = Paginator(posts, 3)
    page = request.GET.get("p")
    posts = paginator.get_page(page)
    return render(request, "posts/index.html", {"posts": posts})


# Função que pega um dado no banco de dados e se não existir levanta um erro 404.
def ver_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    return render(request, "posts/ver_post.html", {"post": post})


# Comentario
def Comentario(request):
    # Validando o formulário caso não tenha sido postado nada.
    if request.method != "POST":
        messages.info(request, "Nada postato!")
        return render(request, "ver_post.html")

    # Coletando os dados
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    comentario = request.POST.get("comentario")

    cadastro_comentario = Comentario.object(
        comment_name=nome,
        comment_email=email,
        comment=comentario,
    )

    cadastro_comentario.save()
    return redirect("posts/ver_post.html")
