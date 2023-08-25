from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='main'),
    path('developers/',views.AboutDevelopersPage.as_view(), name='developers'),
    path('commands/',include('commands.urls')),
    path('accounts/', include('users.urls')),
]