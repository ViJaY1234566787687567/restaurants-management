"""
URL configuration for delivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static
app_name="shop"

urlpatterns = [

    path('',views.allcategories,name="allcat"),
    path('allprod/<p>',views.allproducts,name="allprod"),
    path('details/<c>',views.details,name="details"),
    path('register',views.register,name="register"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
