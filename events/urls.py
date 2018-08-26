from django.urls import path
from . import views
from register import views as rviews

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', rviews.rindex, name='rindex'),

]
