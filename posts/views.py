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

from django.views.generic.edit import UpdateView
from comentarios.models import Comment
# from comentarios.forms import FormCommentModel
from comentarios.forms import FormComment



def index(request):
    posts = Posts.objects.order_by("id").filter(post_published=True)
    paginator = Paginator(posts, 3)
    page = request.GET.get("p")
    posts = paginator.get_page(page)
    return render(request, "posts/index.html", {"posts": posts})


# Função que pega um dado no banco de dados e se não existir levanta um erro 404.
def ver_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    
    # nova funcionalidade, exibir os comentários nos posts.
    comment = Comment.objects.order_by("id").filter(comment_published=True)

    # Coletando os dados
    if str(request.method) == 'POST':
        
        form = FormComment(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Comentário enviado com sucesso.')
            form = FormComment()
       
        else:
            messages.success(request, 'Erro ao enviar comentário.')
    else:
        form = FormComment()
   
    return render(request, "posts/ver_post.html", 
                  {"post": post, "comment": comment,
                  "form": form})












