from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forum/<str:loc>', views.forum, name='forum'), 
    path('login', views.mylogin, name='login'),
    path('logout', views.mylogout, name='logout'),
    path('register', views.myregister, name='register'),
    path('new', views.newcomplaint, name='newcomplaint'),
    path('forum/upvote/<str:cid>/<str:uid>', views.upvote, name='upvote'),
    path('forum/solve/<str:cid>', views.solve, name='solve'),   
    path('forum/delete/<str:cid>', views.delete, name='delete'),
]