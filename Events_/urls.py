from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('events/', include('events.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('login/', include('login.urls')),

]


