"""cafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from coffee import views
from django.contrib import admin
from django.urls import path
from coffee import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('review/', views.review, name='review'),
    path('delete/<int:id>',views.destroy),
    path('show/', views.show),
    path('cl/', views.cl,name='cl'),
    path('delete/<int:id>',views.destroy),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('il/', views.il,name='il'),
    path('login/' ,views.login,name='login'),
    path('register/', views.rl,name='rl'),
    # path('login/', views.login, name='login.html'),

    path('', views.ImageUploaderProject),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #database ke sth media name k folder me jare ha











