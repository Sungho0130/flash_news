from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

def main_page(request):
    return render(request, "main.html")
