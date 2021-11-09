
from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # solo envio de token
    # path('api-auth/', include('rest_framework.urls')),
    
    # obtiene el token cuando el usuario envia el mail y password
    # path('api/token/', obtain_auth_token, name='obtain-token'),

    # get y post
    path('articles/', ArticleView.as_view()),

    # get
    path('detalle/<int:id>', DetalleView.as_view()),

    # post
    path('detalle/', AddDetalleView.as_view()),

    # third party packages
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
