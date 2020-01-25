from django.shortcuts import render
from django.views import generics
from django.contrib.auth.model import Groups


class GroupsListView(generics.ListView):
    model = Groups
    template_name = 'simple_list.html'
    

class GroupsCreateView(generics.CreateView):
    model = Groups
    template_name = 'simple_form.html'
    success_url = reverse_lazy('group-list')


class GroupsUpdateView(generics.UpdateView):
    model = Groups
    template_name = 'simple_form.html'
    success_url = reverse_lazy('group-list')


class GroupsDeleteView(generics.DeleteView):
    model = Groups
    template_name = 'simple_form.html'
    success_url = reverse_lazy('group-list')

