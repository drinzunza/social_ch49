from django.urls import path
from .views import CreateNoteView, ListNotesView, DetailNoteView, DeleteNoteView, UpdateNoteView

urlpatterns = [
    path("create/", CreateNoteView.as_view(), name="create_note"),
    path("list/", ListNotesView.as_view(), name="list_notes"),
    path("details/<int:pk>/", DetailNoteView.as_view(), name="detail_note"),
    path("delete/<int:pk>/", DeleteNoteView.as_view(), name="delete_note"),
    path("update/<int:pk>/", UpdateNoteView.as_view(), name="update_note"),
]
