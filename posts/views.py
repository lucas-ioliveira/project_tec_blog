# Importação dos módulos do Django para renderizar meu html e levantamento de erros
from django.shortcuts import render, get_object_or_404, redirect , reverse

# Importação levantamento de erros
from django.http import Http404

# Importação do meu módulo de Posts
from .models import Posts

# Importação do módulo do Django para paginação
from django.core.paginator import Paginator

# Importação do módulo do Django
from django.contrib import messages
from comentarios.forms import FormCommentModel
from comentarios.models import Comment



def index(request):
    posts = Posts.objects.order_by("id").filter(post_published=True)
    paginator = Paginator(posts, 3)
    page = request.GET.get("p")
    posts = paginator.get_page(page)
    return render(request, "posts/index.html", {"posts": posts})



def ver_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    comment = Comment.objects.order_by("id").filter(comment_published=True)
    form = FormCommentModel(request.POST or None)
   
    # Coletando e realizando a verificação do id
    post_ids = Comment.objects.all().order_by("-id")
    if not post_ids:
        new_post_id = 1
    else:
        new_post_id = Comment.objects.all().order_by("-id")[0].id + 1

    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.instance.id = new_post_id
            form.save()
            return redirect(reverse('index'))
            
    context = {
        'post':post,
        'comment':comment,
        'form':form,
    }
    return render(request, "posts/ver_post.html", context)














