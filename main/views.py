from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import *
from .forms import ContactForm
from django.urls import reverse



class index(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        qs = Index.objects.all()
        return qs

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data ['contact'] = Contact.objects.all()
        data ['testemonila'] = Testemonial.objects.all()
        data ['historytitle'] = HistoryTitle.objects.all()
        data ['history'] = History.objects.all()
        data ['about'] = About.objects.all()
        return data 


class ContactFormView(CreateView):
    template_name = 'index.html'
    form_class = ContactForm
    
