from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path('your-model-endpoint/', views.your_model_endpoint, name='your-model-endpoint'),
    path("ns_page", views.ns_page, name="ns_page"),

]