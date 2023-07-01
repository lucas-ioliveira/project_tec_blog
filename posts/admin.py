from django.contrib import admin
from .models import Categoria, Posts

# Modificando exibição


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "post_title",
        "post_author",
        "post_date",
        "post_category",
        "post_published",
    )
    list_editable = ("post_published",)
    list_display_links = ("id", "post_title")


# Registrando os modelos no admin do Django.
admin.site.register(Categoria)
admin.site.register(Posts, PostAdmin)
