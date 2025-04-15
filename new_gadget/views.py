from django.shortcuts import render
from new_gadget import models
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django .urls import reverse_lazy
# Create your views here.

class show(ListView):
    model = models.Gadget_table
    template_name = 'all_gadgets.html'
    context_object_name = 'gadgets' 

class create(CreateView):
    model = models.Gadget_table
    fields = ['model','picture','price','about']
    template_name = 'create.html'
    success_url = reverse_lazy('show_all')

class Edit(UpdateView):
    model = models.Gadget_table
    fields = ['model','picture','price','about']
    template_name = 'create.html'
    success_url = reverse_lazy('show_all')
    pk_url_kwarg = 'pk'
    context_object_name = 'gadget' 


class Delete(DeleteView):
     template_name = "delete.html"
     model = models.Gadget_table
     success_url = reverse_lazy('show_all')
     pk_url_kwarg = 'pk'

