from django.urls import path
from . import views

app_name='thread'

urlpatterns=[
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('catalog/', views.thread_list, name='list'),
    path('thread/create/', views.thread_create, name='create'),
    path('thread/<int:id>/', views.thread_details, name='details'),
    path('thread/<int:id>/comment/', views.thread_comment, name='comment'),
    path('thread/<int:id>/comment/<int:id2>/', views.reply, name='reply'),
]
