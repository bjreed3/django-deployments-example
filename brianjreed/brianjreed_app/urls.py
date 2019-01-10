from django.conf.urls import url
from brianjreed_app import views

#for template Tagging

app_name = 'brianjreed_app'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    url(r'^AboutMe/$',views.aboutme,name='aboutme'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
