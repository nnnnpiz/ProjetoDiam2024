from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)


app_name = 'romax' #acho que isto nao é necessario pq so vamos ter uma app!!
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('pesquisa_avancada/', views.pesquisa_avancada, name='pesquisa_avancada'),
    path('resultados_pesquisa/', views.resultados_pesquisa, name='resultados_pesquisa'),
    path('propriedade/<int:id>/', views.propriedade, name='propriedade'),
    path('login/', views.login, name='login'),
    path('criar_conta_page/', views.criar_conta_page, name='criar_conta_page'),
    path('criar_conta', views.criar_conta, name='criar_conta')
    path('criar_conta/', views.criar_conta, name='criar_conta'),
]

