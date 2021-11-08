from django.contrib import admin

# Register your models here.


from .models import Article, Detalle

admin.site.register(Article)


admin.site.register(Detalle)