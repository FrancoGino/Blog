from django.shortcuts import render
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from post.models import Post

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

class RegistrarUsuario(CreateView):
    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'crear_post.html'
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ListarPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'listar_post.html'

    def get_queryset(self):
        return Post.objects.filter(autor = self.request.user)
    
class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('listar_post.html')

    def get_queryset(self):
        return Post.objects.filter(autor = self.request.user)
    
class EditarPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'editar_post.html'

    success_url = reverse_lazy('listar_posts')

    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)


class DetallePost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detalle_post.html'

    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)