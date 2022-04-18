"""kelajak_yoshlari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from kelajak_yoshlariapp.views import *
from django.conf  import  settings
from  django.conf.urls.static  import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg', registerUser, name='r'),
    path('logins', loginUsers, name='login'),
    path('', dashboard, name='dashboard'),
    path('dash', dashboard2, name='dash'),
    path('dashb', dashboard3, name='dashb'),
    path('viktoria', abaut, name='ab'),
    path('musobaqa', musobaqa, name="m"),
    path('savol_javob_sahifasi', savol_javob_sahifasi, name="s"),
    path('savollar', savollar, name="savol"),
    path('javob', javob, name="javob"),
    path('ba', batafsil, name='b'),
    path('aloqa', aloqa, name='aloqaa'),
    path('comment', comment, name='coms'),
    path('kurslar', masofaviy_oquv_kursi, name='curs'),
    path('dasturlash', dasturlash, name='dasturlash'),
    path('tarix', tarix, name='tarix'),
    path('matem', matematika, name='matem'),
    path('reyting', reytinglar, name='res'),
    path('chat', chat, name='chat'),
]
if  settings.DEBUG:
    urlpatterns  +=  static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

