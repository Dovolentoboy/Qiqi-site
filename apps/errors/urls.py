from django.urls import path,include
from . import views

urlpatterns = [
    path('404/', views.Page404.as_view(), name='404'),
]