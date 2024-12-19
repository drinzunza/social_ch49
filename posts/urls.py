from django.urls import path
from .views import ListPostsView, CreatePostView, SaveCommentView, ListBookmarkView, SaveBookmarkView
from .views import DeleteBookmarkView, DeletePostView

urlpatterns = [
    path('list/', ListPostsView.as_view(), name="list_posts"),
    path('create/', CreatePostView.as_view(), name="create_post"),
    path('save_comment/', SaveCommentView.as_view(), name="save_comment"),
    path('bookmarks/', ListBookmarkView.as_view(), name="bookmarks"),
    path('save_bookmark/', SaveBookmarkView.as_view(), name="save_bookmark"),
    path("delete_bookmark/<int:pk>/", DeleteBookmarkView.as_view(), name="delete_bookmark"),
    path('delete_post/<int:pk>/', DeletePostView.as_view(), name="delete_post"),
]
