from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

@login_required
def addPost(request):
    if request.method == 'POST':
        post_Form = forms.postForm(request.POST)
        if post_Form.is_valid():
            # post_Form.cleaned_data['author'] = request.user
            post_Form.instance.author = request.user
            post_Form.save()
            return redirect('addPost')
    else:
        post_Form = forms.postForm()

    return render(request, 'addPosts.html', {'form':post_Form})

# Add post using class based view

@method_decorator(login_required, name='dispatch')
class addPostCreateView(CreateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'addPosts.html'
    success_url = reverse_lazy('addPost')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

@login_required
def editPost(request, id):
    post = models.Post.objects.get(pk=id)
    post_Form = forms.postForm(instance=post)
    if request.method == 'POST':
        post_Form = forms.postForm(request.POST, instance=post)
        if post_Form.is_valid():
            post_Form.instance.author = request.user            
            post_Form.save()
            return redirect('homepage')

    return render(request, 'addPosts.html', {'form':post_Form})

@method_decorator(login_required, name='dispatch')
class editPostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'addPosts.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


@login_required
def deletePost(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

@method_decorator(login_required, name='dispatch')
class deletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile') 
    pk_url_kwarg = 'id'

class detailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'postDetails.html'

    def post(self, request, *args, **kwargs):
        comment_Form = forms.commentForm(data=self.request.POST)
        post = self.get_object()
        if comment_Form.is_valid():
            newComment = comment_Form.save(commit=False)
            newComment.post = post
            newComment.save()
        return self.get(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_Form = forms.commentForm()

        context['comments'] = comments
        context['comment_Form'] = comment_Form

        return context
