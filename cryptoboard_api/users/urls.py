from django.conf.urls import url
from users import views

# Template Tagging
app_name = 'users'

urlpatterns = [
    url(r'logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'user_login/$', views.user_login, name='user_login'),
]
