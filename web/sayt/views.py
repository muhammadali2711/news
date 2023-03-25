from django.shortcuts import render
from .models import Category, News

# Create your views here.
def index(requests):
    ctgs = Category.objects.all()
    news = News.objects.all()
    jahon_ctg = Category.objects.get(slug="jahon")
    jahon_news = News.objects.filter(ctg=jahon_ctg)
    uzbek_ctg = Category.objects.get(slug="uzbekistan")
    uzbek_news = News.objects.filter(ctg=uzbek_ctg)




    ctx = {
        "ctgs": ctgs,
        "news": news,
        "jahon_news": jahon_news,
        "uzbek_news": uzbek_news

    }

    return render(requests,"index.html", ctx)

def category(requests, slug):
    ctgs = Category.objects.all()
    ctg = Category.objects.get(slug= slug)
    news = News.objects.all().filter(ctg_id=ctg.id)
    ctx = {
        "ctgs": ctgs,
        "ctg": ctg,
        "news": news

    }
    return render(requests,"category.html", ctx)

def search (requests):
    ctx = {

    }
    return render(requests,"search.html", ctx)

def view(requests, pk):
    ctgs = Category.objects.all()
    new = News.objects.get(pk=pk)
    news = News.objects.all()

    ctx = {
        "ctgs": ctgs,
        "new": new,
        "news": news

    }
    return render(requests, "view.html", ctx)

def contact(requests):
    ctx = {

    }
    return render(requests,"contact.html", ctx)
