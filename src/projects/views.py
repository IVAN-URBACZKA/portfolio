from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ProjectPost
from django.contrib.auth.decorators import login_required

class ProjectPostHomeView(ListView):
    model = ProjectPost
    context_object_name = "projects"
