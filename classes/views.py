from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

class CBView(View):
    def get(self,request):
        return render(request, 'classes/index.html')


def index(request):
    return render(request, 'classes/index.html')


def base(request):
     return render(request, 'classes/base.html')

class TemV(TemplateView):
     template_name = 'classes/index.html'

     def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         context['injectme'] = 'BASIC INJECTION'
         return context
