from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("ns_page", views.ns_page, name="ns_page"),
    path('<str:category>/', views.detail_page, name='category_news'),
]