from django.contrib import admin
from django.urls import path, include
from apps.studytracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('apps.authentication.urls')),
    path('', views.top, name='top'),
    path('studytracker/', include('apps.studytracker.urls')),
]
