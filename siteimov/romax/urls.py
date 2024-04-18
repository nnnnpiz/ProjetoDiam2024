from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)


app_name = 'romax' #acho que isto nao é necessario pq so vamos ter uma app!!
urlpatterns = [

#ex: /
    path('', views.landing_page, name='landing_page'),
    path('pesquisa_avancada/', views.pesquisa_avancada, name='pesquisa_avancada'),
    path('resultados_pesquisa/', views.resultados_pesquisa, name='resultados_pesquisa'),
    path('propriedade/', views.propriedade, name='propriedade'),

]

