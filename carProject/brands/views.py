from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.

class addBrandsCreateView(CreateView):
    model = models.Brands
    form_class = forms.brandsForm
    template_name = 'addBrands.html'
    success_url = reverse_lazy('addBrands')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    