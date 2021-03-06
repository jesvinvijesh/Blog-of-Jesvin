from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/delete', delete, name="delete"),
    path('<slug>/edit/', edit_blog_view, name="edit"),
 ]