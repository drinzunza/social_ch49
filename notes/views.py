from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .forms import NoteForm
from .models import Note

# Create your views here.
"""
    View = generic view
    ListView = get a list of records
    DetailView = get the details of a record
    CrateView = create a new record
    DeleteView = delete record
    UpdateView = update record
    LoginView = login 
"""

class CreateNoteView(CreateView):
    template_name = "notes/create_note.html"
    form_class = NoteForm

    def get_success_url(self):
        return reverse('list_notes')
    

class ListNotesView(ListView):
    template_name = "notes/list_note.html"
    model = Note


class DetailNoteView(DetailView):
    template_name = "notes/detail_note.html"
    model = Note


class DeleteNoteView(DeleteView):
    template_name = "notes/delete_note.html"
    model = Note

    def get_success_url(self):
        return reverse("list_notes")
    

class UpdateNoteView(UpdateView):
    template_name = "notes/update_note.html"
    model = Note
    form_class = NoteForm

    def get_success_url(self):
        return reverse("list_notes")