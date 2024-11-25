from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('', views.posts,name="posts_list"),
    path('new-post/', views.posts_new,name="new-post"),
    path('<slug:slug>', views.post_page,name="page"),

]
