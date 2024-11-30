from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    # представления поста
    path('', views.project_list, name='project_list'),
    path('<int:id>/', views.project_detail, name='project_detail'),
]
