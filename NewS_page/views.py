from django.shortcuts import render, redirect
from .models import Crawring
from .news_craw import newscrawring
from .model_call import summary
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time

def main_page(request):

    craw =Crawring.objects.exclude(summarize='').order_by('-created_at')[:20]

    return render(request, "main.html", {'craw': craw})










