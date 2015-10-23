from django.shortcuts import render

from django.views.generic import TemplateView

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class Home(TemplateView):
  template_name = "home.html"

class MessageCreateView(CreateView):
  model = Message
  template_name = "message/message_form.html"
  fields = ['email', 'message']
  success_url = reverse_lazy('home')
