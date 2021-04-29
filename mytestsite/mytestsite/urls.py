from django.contrib import admin
#from django.conf.urls import *
#from django.contrib.auth.views import login
from .views import *
from django.conf.urls import url, include

urlpatterns = [
 #   url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    
    url(r'^directorio/', include('directorio.urls')),
    url(r'^login/', login, {'template_name':'login.html'}, name='login'),
  #  url(r'^logout/', logout_then_login, name='logout'),

 #   url('persona/', include('directorio.urls')),
    url('accounts/login/', autenticar, name='login'),
    url('logout/', logoutView, name='logout'),
    url(r'^inicio/$', inicio ,name='inicio'),


    
]
