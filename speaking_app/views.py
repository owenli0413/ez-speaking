from django.views.generic import TemplateView, CreateView
from .models import Messages
from .forms import MessagesForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.utils.translation import gettext_lazy

from pathlib import Path
from django.http import HttpRequest
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'home.html'

def TestView(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    dataset = {
        'path': BASE_DIR
    }
    return render(request,'test.html', context=dataset)

class MessagesCreateView(SuccessMessageMixin,CreateView):
    model = Messages
    form_class = MessagesForm
    template_name = "messages_form.html"
    success_url = reverse_lazy('contact form')
    success_message = gettext_lazy("Message sent successfully")
