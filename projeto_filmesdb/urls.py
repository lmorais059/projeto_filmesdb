
from django.urls import include, path
from app_filmesdb import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('home', views.home, name='home'),
    path('filmes/', views.filmes, name='filmes'),
    path('delete_filme/<int:id_filme>', views.delete_filme, name='delete_filme'),
    path('detalhes_filme/<int:id_filme>', views.detalhes_filme, name='detalhes_filme'),
    path('editar_filme/<int:id_filme>', views.editar_filme, name='editar_filme'),
    path('classificar_filme/<int:id_filme>', views.classificar_filme, name='classificar_filme'),
    path('adicionar_comentario/<int:id_filme>', views.adicionar_comentario, name='adicionar_comentario'),
    path('trailers/', views.trailers, name='trailers'),
    path('search_filmes/', views.search_filmes, name='search_filmes'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro')
]
