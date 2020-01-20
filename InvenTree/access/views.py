from django.shortcuts import render
from django.views import generics
from django.contrib.auth.model import Groups

class GroupsCreateView(generics.CreateView):
    model = Groups
    template_name = 'simple_form.html'
    success_url = 



