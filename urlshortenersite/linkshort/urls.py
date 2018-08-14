from django.urls import path
from . import views

app_name = 'linkshort' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:shortened>/', views.shorten_redirect, name='redirect')
]