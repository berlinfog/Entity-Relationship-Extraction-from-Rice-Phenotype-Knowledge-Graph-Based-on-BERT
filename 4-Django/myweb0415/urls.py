"""myweb0415 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url 
from django.urls import path
from . import relation_view
from . import homepage
from weblrl import views
from django.views.static import serve
from django.conf.urls import include
urlpatterns = [
    url(r'^$',homepage.homepage),
    url(r'^search_entity',relation_view.search_entity),
    url(r'^relation_extract',relation_view.relation_extract),


    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha', include('captcha.urls')),  # 增加这一行
    url(r'^detail/', views.detail),
    url(r'^ask/', relation_view.ask),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':'C:\\Users\10750\Desktop\fourth\bishe\prosess_record\5Server\study\myweb0415\static'}),
]
