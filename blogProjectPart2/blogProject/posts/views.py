from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

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

@login_required
def deletePost(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')