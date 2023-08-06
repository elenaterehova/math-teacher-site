from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_number, name='post_number'),
    path('post/study', views.post_study, name='study'),
    path('https://web.telegram.org/k/', views.telegram, name='telegram'),
    path("https://vk.com/", views.vk, name='vk'),
    path('https://www.whatsapp.com/?lang=ru_RU', views.whatsapp, name='whatsapp'),
    path('https://discord.com/', views.discord, name='discord'),
    path('https://mail.ru/', views.mail, name='mail'),


]
