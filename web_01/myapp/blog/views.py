from django.shortcuts import render
import requests as req

base_url = 'https://dummyjson.com/posts'


# Create your views here.

def blog_list(request):
    res = req.get(base_url)
    if res.status_code == 200:
        result = res.json()
    else:
        result = {}
    return render(request, 'blog/list.html', result)


def detail(request, blog_id: int):
    res = req.get(f"{base_url}/{blog_id}")
    if res.status_code == 200:
        result = res.json()
    else:
        result = {}
    return render(request, 'blog/detail.html', result)
