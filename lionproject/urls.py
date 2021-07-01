"""lionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django import urls
from django.contrib import admin
from django.urls import path, include #include 함수
from blog.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ #view에 함수가 추가할때마다 적기
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('blog/', include('blog.urls')), #blog(app)에 있는 urls를 포함하겠다!
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #이건 계속 복붙
