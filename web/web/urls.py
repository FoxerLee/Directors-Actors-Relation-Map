"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from relation1.views import detail, search
from relation2.views import relation2, search2
from relation3.views import relation3, search3
from web import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.index),
    url(r'^relation1/', detail),
    url(r'^search1/', search, name='search'),
    url(r'^relation2/', relation2),
    url(r'^search2/', search2),
    url(r'^relation3/', relation3),
    url(r'^search3/', search3),
]
