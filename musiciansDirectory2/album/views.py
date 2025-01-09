from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from . import forms
from . import models

# Create your views here.

@method_decorator(login_required, name='dispatch')
class addAlbumView(CreateView):
    model = models.Album
    form_class = forms.albumForm
    template_name = 'addAlbum.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class editAlbumView(UpdateView):
    model = models.Album
    form_class = forms.albumForm
    template_name = 'editAlbum.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        return super().form_valid(form)


@login_required
def deleteAlbum(request, id):
    post = models.Album.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
