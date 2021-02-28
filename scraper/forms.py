from django import forms

class CrawlerForm(forms.Form):
    website = forms.CharField(label="website", max_length=200)
