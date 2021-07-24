from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now) #sets datetime to when post was created or when i want to change
    author=models.ForeignKey(User,on_delete=models.CASCADE) #delete the post when the user is deleted(not vice verse)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # this is to redirect to the detail page for the post after post creation
        return reverse("post-detail", kwargs={"pk": self.pk})
        

           