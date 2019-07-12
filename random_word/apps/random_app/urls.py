from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^random_word$', views.random),
    url(r'^generate$', views.generate),
]