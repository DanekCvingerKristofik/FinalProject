"""FinalProject URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import places.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', places.views.home, name = "home"),
    path('trip/<int:id>/', places.views.trip, name = "trip"),
    path('hotel/<int:id>/', places.views.hotel, name = "hotel"),
    path('search/', places.views.search, name = "search"),
    path('purchase_create/', places.views.PurchaseCreateView.as_view(), name='purchase_create'),
    path('accounts/signup/', places.views.SignUpView.as_view(), name='signup'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('your_purchase/', places.views.your_purchase, name='your_purchase'),
    path('profil/', places.views.profil, name='profil')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

