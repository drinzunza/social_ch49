from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Post, Reactions, Comment, Bookmark
from .forms import PostForm, ReactionForm, CommentForm
from django.urls import reverse, reverse_lazy
from users.models import Profile
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect

# Create your views here.
class ListPostsView(ListView):
    template_name = "posts/list_posts.html"
    model = Post
    context_object_name = 'post_list'

    def get_queryset(self):
        data = super().get_queryset().order_by('-created_on').prefetch_related('comments')
        for post in data:
            post.author_profile = Profile.objects.filter(user=post.author).first()
            post.likes = Reactions.objects.filter(post=post).filter(react_type='like').count()
            post.dislikes = Reactions.objects.filter(post=post).filter(react_type='dislike').count()
            post.hearts = Reactions.objects.filter(post=post).filter(react_type='heart').count()
        return data
    

    def post(self, request, *args, **kwags):
        # handle reactions
        form = ReactionForm(request.POST)
        if form.is_valid():
            react_type = form.cleaned_data['react_type']
            post_id = request.POST.get('post_id')
            post = Post.objects.get(id=post_id)

            # create the reaction
            Reactions.objects.update_or_create(
                user=request.user,
                post=post,
                defaults={'react_type': react_type}
            )
            return redirect('list_posts')



class CreatePostView(CreateView):
    template_name = "posts/create_post.html"
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse('list_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user # logged in user
        return super().form_valid(form)
    

class SaveCommentView(CreateView):
    
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get("post_id")
        comment_text = request.POST.get('text')
        
        # get the post
        post = Post.objects.get(id=post_id)
        user = request.user

        # create the comment
        comment = Comment.objects.create(
            text = comment_text,
            post = post,
            user = user
        )

        # return a json respose 
        return JsonResponse({
            'status': 'success',
            'comment': {
                'id': comment.id,
                'text': comment.text,
                'user': comment.user.username,
                'created_on': comment.created_on
            }
        })


class ListBookmarkView(ListView):
    template_name = "posts/list_bookmark.html"
    model = Bookmark

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)


class SaveBookmarkView(CreateView):
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get("post_id")
        title = request.POST.get("title")

        # get post
        post = Post.objects.get(id=post_id)
        user = request.user

        bookmark = Bookmark.objects.create(
            title=title,
            post=post,
            user=user
        )

        # return success
        return JsonResponse({
            'status': 'success',
        })
    

class DeleteBookmarkView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmarks')

    def get(self, request, *args, **kwargs):
        # skip confirmation page
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)