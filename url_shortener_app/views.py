from django.shortcuts import render,redirect
from url_shortener_app.models import Urlsdb
from url_shortener.settings import SITE_URL
from urllib.parse import urlparse
from django.contrib import messages
import random
import string
def is_valid_url(text):
    try:
        result = urlparse(text)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    
def url_shortener_view(request):
    if request.method=="POST":
        long_url=request.POST.get("longurl")
        if is_valid_url(long_url):
            check = Urlsdb.objects.filter(long_url=long_url)
            if check:
                short_url=Urlsdb.objects.get(long_url=long_url).short_url
                shortened_url=SITE_URL + '/' + short_url
                return render(request,"url_shortener_app/homepage.html",{
                "shortened_url":shortened_url,
                "long_url":long_url,
                "short_url":short_url,
            })
            def generate_short_url(length=5):
                characters = string.ascii_letters + string.digits
                return ''.join(random.choice(characters) for _ in range(length))
            def shorten_url():
                while True:
                    short_url = generate_short_url(5)
                    check = Urlsdb.objects.filter(short_url=short_url)
                    if not check:
                        return short_url
            short_url=shorten_url()
            new_url=Urlsdb(long_url=long_url,short_url=short_url)
            new_url.save()
            shortened_url=SITE_URL + '/' + short_url
            return render(request,"url_shortener_app/homepage.html",{
                "shortened_url":shortened_url,
                "long_url":long_url,
                "short_url":short_url,
            })
        else:
            redirect("homepage")
    return render(request,"url_shortener_app/homepage.html")

def url_redirect_view(request,short_url):
    try:
        new_url=Urlsdb.objects.get(short_url=short_url)
        return redirect(new_url.long_url)
    except:
        return redirect('homepage')

def display_urls(request):
    urls=Urlsdb.objects.all()
    return render(request,"url_shortener_app/list.html",{"urls":urls,"siteurl":SITE_URL})


# Create your views here.
