import random

from django.shortcuts import render
from django.http import JsonResponse
from .models import Paste
from .form import *


def add(request):
    if request.method != 'POST':
        return JsonResponse({"status": "bad_method"})
    form = PasteForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"status": "bad_form"})
    content = form.cleaned_data['content']
    title = f'{random.randrange(0, 1000000):06}'
    paste = Paste(title=title, content=content)
    paste.save()
    return render(request, 'pastebin/code.html', {"code": title})


def get(request):
    if request.method != 'POST':
        return JsonResponse({"status": "bad_method"})
    form = CodeForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"status": "bad_form"})
    title = form.cleaned_data['title']
    try:
        paste = Paste.objects.get(title=title)
    except Paste.DoesNotExist:
        return render(request, 'pastebin/notfound.html')
    content = paste.content
    return render(request, 'pastebin/content.html', {"content": content})


def index(request):
    return render(request, 'pastebin/index.html')


def css(request):
    return render(request, 'pastebin/style.css', content_type='text/css')
