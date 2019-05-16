"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static  # importation of any static files
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import TemplateView

from blog import views
app_name = 'blog'


urlpatterns = [
    path('', lambda request: redirect('blog/', permanent=False)),
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('blog/templates/mydatahistory', views.get_data_db, name='mydatahistory'),
    path('blog/templates/refreshquotes', views.refresh_quotes, name="datadbrefreshed"),
    path('blog/delete-row/', views.delete_row, name="deleterow"),
    path('blog/add-isin/', views.add_row),
    path('blog/add-place/', views.add_row),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # for the static files