from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import CrawlerForm

# That code probably shouldn't even been pushed on GitHub. I intended to make an app
# without a model, just for practice, so decided to make a crawler, which should
# return a list of links. And it works, but only for links between the <li> tag.
# Definitely won't work in many cases. It's obviously too simple, and I'm not going to
# work on it anymore, for it is only an excercise.

def show_list(request):
    alert = "Paste a link to a website you want to search"

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

            plain = data.content
            results = BeautifulSoup(plain, "html.parser")
            #Finding all results with given tag
            links = results.findAll('li')
            #Initializing an empty list of items
            items=[]
            for link in links:
                a = link.find('a',href=True)
                if a is None:
                    continue
                else:
                    a = a['href']
                    items.append(a)
            return render(request,"index.html",{'alert':alert, 'data':data, 'items':items})
    else:
        form = CrawlerForm()
    return render(request,"index.html",{'alert':alert, 'form':form})
