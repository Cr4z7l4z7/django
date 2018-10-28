from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import AccessRecord, Topic, WebPage
from . import forms
from my_app.sing_up import new_user


def new_user_form(request):
    forma = new_user()

    if request.method == "POST":
        forma = new_user(request.POST)
        if forma.is_valid():
            forma.save(commit=True)
            return index(request)
        else:
            print("ERROR FROM INVALID")
    return render (request, 'my_app/signup.html', {'forma':forma})

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render (request, 'my_app/index.html', context = date_dict)

def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print('VALIDATION SUCCESS!')
            print('NAME: '+form.cleaned_data['name'])
            print('EMAIL: '+form.cleaned_data['email'])
            print('TEXT:  '+form.cleaned_data['text'])
    return render(request, 'my_app/form_page.html',{'form':form})
