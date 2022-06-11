import random
import time

from django.shortcuts import render
from django.http import JsonResponse
from .models import Paste
from .form import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add(request):
    if request.method != 'POST':
        return JsonResponse({"status": "bad_method"})
    form = PasteForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"status": "bad_form"})

    content = form.cleaned_data['content']
    expire = int(time.time()) + 7 * 24 * 3600
    collision = True
    while collision:
        try:
            title = f'{random.randrange(0, 10000000):07}'
            paste = Paste.objects.get(title=title)
            if time.time() > paste.expire:
                collision = False
        except Paste.DoesNotExist:
            collision = False
    paste = Paste(title=title, content=content, expire=expire)
    paste.save()
    return render(request, 'pastebin/code.html', {"code": title})


@csrf_exempt
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
    if time.time() > paste.expire:
        return render(request, 'pastebin/notfound.html')
    content = paste.content
    return render(request, 'pastebin/content.html', {"content": content})


def index(request):
    return render(request, 'pastebin/index.html')


def css(request):
    return render(request, 'pastebin/style.css', content_type='text/css')
