from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

# commenting these parts because I am managing cars through Django admin panel

# @method_decorator(login_required, name='dispatch')
# class addCarsCreateView(CreateView):
#     model = models.Cars
#     form_class = forms.carsForm
#     template_name = 'addCars.html'
#     success_url = reverse_lazy('addCars')
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# @method_decorator(login_required, name='dispatch')
# class editCarsUpdateView(UpdateView):
#     model = models.Cars
#     form_class = forms.carsForm
#     template_name = 'addCars.html'
#     pk_url_kwarg = 'id'
#     success_url = reverse_lazy('profile')

# @method_decorator(login_required, name='dispatch')
# class deleteCarsView(DeleteView):
#     model = models.Cars
#     template_name = 'delete.html'
#     success_url = reverse_lazy('profile') 
#     pk_url_kwarg = 'id'

class detailCarsView(DetailView):
    model = models.Cars
    pk_url_kwarg = 'id'
    template_name = 'carsDetails.html'

    def post(self, request, *args, **kwargs):
        comment_Form = forms.commentForm(data=self.request.POST)
        cars = self.get_object()
        if comment_Form.is_valid():
            newComment = comment_Form.save(commit=False)
            newComment.car = cars
            newComment.save()
        return self.get(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars = self.object
        comments = cars.comments.all()
        comment_Form = forms.commentForm()

        context['comments'] = comments
        context['comment_Form'] = comment_Form

        return context
    
def buyNow(request, car_id):
    car = models.Cars.objects.get(id=car_id)

    if car.quantity > 0:
        car.quantity -= 1
        car.purchasedBy.add(request.user)
        car.save()
        messages.success(request, f'{car.name} has been added to your profile!')
    else:
        messages.error(request, 'This car is out of stock.')

    return redirect('profile')