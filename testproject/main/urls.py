from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^main', views.get_main, name='get_main')
]
