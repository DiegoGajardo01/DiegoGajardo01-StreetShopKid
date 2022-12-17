"""StreetShopKid URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from StreetShopKidApp import views

from django.conf import settings
from django.conf.urls.static import static 

app_name='StreetShopKidApp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('categorias/<slug>', views.buscar_categoria, name="categorias"),
    path('search', views.search, name="search"),
    path('detail/<slug>', views.detail, name="detail"),
    path('<slug>/carro', views.carro, name="carro"),
    path('micarro', views.micarro, name="micarro"),
    path('agregar-producto/', views.agregarProducto, name="agregarProducto"),
    path('listar-productos/', views.listarProductos, name="listarProducto"),
    path('modificar-producto/<id>/', views.modificarProducto, name="modificarProducto"),
    path('eliminar-producto/<id>/', views.eliminarProducto, name="eliminarProducto"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name="registro"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
