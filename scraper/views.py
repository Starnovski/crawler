from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import CrawlerForm

# Create your views here.
def show_list(request):
    alert = "First info"

    if request.method=='POST':
        form = CrawlerForm(request.POST)
        if form.is_valid():
            #Getting an url from form field 'website'
            data =  form.cleaned_data.get('website')
            #Trying to establish connection with given url
            try:
                data = requests.get(data)
            except:
                data = "Can't connect"
            return render(request,"index.html",{'alert':alert, 'data':data})
    else:
        form = CrawlerForm()
    return render(request,"index.html",{'alert':alert, 'form':form})
