from django.shortcuts import render
from django.http import JsonResponse
import json


def add(request):
    paste_data = json.loads(request.body)
    title = paste_data['title']
    content = paste_data['content']
