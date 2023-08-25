from django.contrib import admin
from django.urls import path, include

handler404 = 'errors.views.handler404'
handler403 = 'errors.views.handler403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('users.urls')),
    path('errors/', include('errors.urls'))
]
