from django.conf.urls import url
from first_board import views

# Template tagging
app_name = 'first_board'

urlpatterns = [
    url(r'^cryptos/$', views.cryptos, name='cryptos'),
    url(r'^help_page/$', views.help_page, name='help_page'),
]
