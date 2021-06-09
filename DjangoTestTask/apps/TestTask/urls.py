from django.urls import path

from . import views

app_name = 'TestTask'
urlpatterns = [
    path('', views.index, name='index'),
    path('addpic', views.addpic, name='addpic'),
    path('<int:pic_id>/', views.exact_pic, name='exact_pic'),
    path('the_new_pic', views.the_new_pic, name='the_new_pic')
]