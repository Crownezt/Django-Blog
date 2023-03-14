from django.urls import path
from . import views


urlpatterns = {
    path('hello/', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    path('welcome/', views.welcome, name='welcome'),
    path('comment/', views.comment, name='comment'),
}

