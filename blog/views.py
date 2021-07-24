from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
# LoginrequiredMixin this will redirect the user to the 
#login page if he is not logged in while post creation

#UserPassesTestMixin ensures that only the author for the post can update that post and not the other user
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView



def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')

    context ={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context) 


class PostListView(ListView):    
    model = Post
    template_name='blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5

class UserPostListView(ListView):    # creates a list view for each user for the post they posted
    model = Post
    template_name='blog/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):    
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields= ['title' ,'content']
    
    def form_valid(self,form):  #this will make the current logged in user as the author of the post created  
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields= ['title' ,'content']
    
    def form_valid(self,form):  #this will make the current logged in user as the author of the post created  
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):  
        #userpassestestmixin will run this function and check wther the author of 
        #that post is updating his post only or not
        
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):    # the mixin should be in series
    model = Post
    success_url='/'
    
    def test_func(self):  
        #userpassestestmixin will run this function and check wther the author of 
        #that post is updating his post only or not
        
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    #return  HttpResponse('<h1>Blog About</h1>')
    return render(request,'blog/about.html',{'title':'About'})   