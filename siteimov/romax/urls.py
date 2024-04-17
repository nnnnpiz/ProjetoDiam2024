from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)


app_name = 'romax' #acho que isto nao é necessario pq so vamos ter uma app!!

urlpatterns = [

#ex: romax/
path("", views.index, name="index"),
]

