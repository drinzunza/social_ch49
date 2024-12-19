from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView
from .forms import SignupForm, ProfileForm
from .models import Profile
from django.views.generic import DetailView
from posts.models import Post

# class-based views
"""
    View = generic view
    ListView = get a list of records
    DetailView = get the details of a record
    CrateView = create a new record
    DeleteView = delete record
    UpdateView = update record
    LoginView = login 
"""

# Create your views here.
class UserLoginView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        # after login, send the user to:
        return reverse('list_posts')
        

def user_logout(request):
    logout(request)
    return redirect('login')


class SignUpView(CreateView):
    template_name = "users/singup.html"
    form_class = SignupForm

    # extend the save function to encrypt the password
    def form_valid(self, form):
        user = form.save(commit=False)
        passw = form.cleaned_data['password']
        user.set_password(passw) # hash/encrypt the password
        user.save()

        # create an empty profile for the new user    
        Profile.objects.create(user=user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class UpdateProfileView(UpdateView):
    model = Profile
    template_name = "users/updateProfile.html"
    form_class = ProfileForm
    
    def get_success_url(self):
        return reverse('home')
    
    def get_object(self):
        # return the Profile record that will be updated
        return Profile.objects.filter(user=self.request.user).first()
    


class ProfileDetailView(DetailView):
    template_name = "users/profile.html"
    model = Profile

    def get_object(self):
        # get the profile using the object id
        user_id = self.kwargs.get('user_id')
        return Profile.objects.filter(user__id=user_id).first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        context['posts'] = Post.objects.filter(author=user).order_by('-created_on')
        return context