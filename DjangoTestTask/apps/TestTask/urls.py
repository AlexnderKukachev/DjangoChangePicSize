from django.urls import path

from . import views

app_name = 'TestTask'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_pic', views.add_pic, name='add_pic'),
    path('<int:pic_id>/', views.exact_pic, name='exact_pic'),
]