from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    video = EmbedVideoField(blank=True, null=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"
    

class Reactions(models.Model):
    REACTION_TYPES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
        ('heart', 'Heart')
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reactions")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    react_type = models.CharField(max_length=10,  choices=REACTION_TYPES)

    def __str__(self):
        return f"{self.user.username} reacted with: {self.react_type} to {self.post}"



class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, null=True)


"""
    create the model for Bookmark
     user
     post
     create_on

     

    add the model to admin
    go into admin and create a couple bookmarks
     

    create a page to list all the booksmarks
    create the view -> ListView
    create the template
    create the url





    create the view to save bookmark

    create the url

    udpate the list page,
    when the user clicks on the button
    we will send an js ajax request to save the bookmark

"""