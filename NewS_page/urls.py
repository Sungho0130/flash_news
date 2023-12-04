from django.urls import path
from . import views
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("send-email", views.email_page, name="email_page"),
    # media 파일을 제공하기 위한 URL 패턴
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # static 파일을 제공하기 위한 URL 패턴
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
