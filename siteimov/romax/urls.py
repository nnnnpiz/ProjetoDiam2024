from django.urls import include, path
from . import views
from .views import LoginView, ComentarioView

# (. significa que importa views da mesma directoria)


app_name = 'romax' #acho que isto nao é necessario pq so vamos ter uma app!!
urlpatterns = [
    path('', views.landing_page, name='landing_page'),

    path('pesquisa_avancada/', views.pesquisa_avancada, name='pesquisa_avancada'),

    path('resultados_pesquisa/', views.resultados_pesquisa, name='resultados_pesquisa'),

    path('propriedade/<int:propriedade_id>/', views.propriedade, name='propriedade'),

    path('login/', views.login_view, name='login_view'),

    path('logout/', views.logout_view, name='logout_view'),

    path('criar_conta_page/', views.criar_conta_page, name='criar_conta_page'),

    path('criar_conta/', views.criar_conta, name='criar_conta'),

    path('informacao_pessoal/', views.informacaopessoal, name='informacaopessoal'),

    path('informacao_pessoal/salvar_alteracoes_conta/', views.salvar_alteracoes_conta, name='salvar_alteracoes_conta'),

    path('backend/ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),

    path('backend/criar_propriedade_pagina/<int:pedido_id>', views.criar_propriedade_pagina, name='criar_propriedade_pagina' ),

    path('sobre_page', views.sobre_page, name='sobre_page'),

    path('favorito/<int:propriedade_id>', views.favorito, name='favorito'),

    path('favoritos_page', views.favoritos_page, name='favoritos_page'),

    path('propriedades_all', views.propriedades_all, name='propriedades_all'),

    path('imoveis_luxo', views.imoveis_luxo, name='imoveis_luxo'),

    path('publicar_propriedade/', views.publicar_propriedade, name='publicar_propriedade'),

    path('pesquisa_avancada/search_avancada_treat', views.search_avancada_treat, name='search_avancada_treat'),

    path('comentarios', views.comentarios, name='comentarios'),

    path('login_react/', LoginView.as_view(), name='login_react'),

    path('comentario/', ComentarioView.as_view(), name='comentario'),

    path('indexReact', views.indexReact, name='indexReact'),

    path('comentarioReact', views.comentarioReact, name='comentarioReact'),
]

