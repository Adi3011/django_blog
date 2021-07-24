from django.urls import path
from . import views
from .views import (PostListView,PostDetailView ,
                   PostCreateView ,PostUpdateView ,
                   PostDeleteView,UserPostListView)  #class based view
from users import views as user_views
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),

    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),

    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'), #int:pk will give our post number as integer
    #template for this is post_detail.html
    
    path('post/new/', PostCreateView.as_view(),name='post-create'), # a template for this will be post_form.html
     
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'), 
    # path to update the post and will use same post_form.html template

    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'), 
    #template will be post_confirm_delete.html

    path('about/', views.about,name='blog-about'),

    path('register/', user_views.register,name='users-register'),

] 
 

# when we are using class based views then we should have a template for
#for that view as named  <app>/<model>_<viewtype>.html  example here
# are app is blog , model is post and viewtype is list 