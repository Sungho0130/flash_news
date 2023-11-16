from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path('your-model-endpoint/', views.your_model_endpoint, name='your-model-endpoint'),
<<<<<<< HEAD
    path("ns_page", views.ns_page, name="ns_page"),

=======
    path('/<str:category>/', views.detail_page, name='category_news'),
>>>>>>> e1c072eb612e3fa570dff6991c07131787332735
]