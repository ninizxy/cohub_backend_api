"""backend URL Configuration

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
# from captcha import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls(title='API Documentation')),
    path('admin/', admin.site.urls),
    path('backend/', include('apps.app_core.urls')),
    path('', include('apps.login.urls')),
    path('', include('apps.link_analys.urls')),
    # path('refresh_captcha/',views.refresh_captcha),
    # path('register/',include('apps.register.urls')),
]
