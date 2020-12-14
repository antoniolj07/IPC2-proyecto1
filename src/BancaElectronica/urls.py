"""BancaElectronica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from home.views import *

from user.views import user_detail_view, register_view, login_view, register_empresa_view

urlpatterns = [
    path('', home_view, name='home'),
    path('cuenta-nueva', nueva_cuenta_view, name="nueva-cuenta"),
    path('estado-cuenta', estado_cuenta_view, name="estado-cuenta"),
    path('cuentas', cuentas_view, name="cuentas"),
    path('transferencia-cuentas-propias', cuentas_propias_view, name="transferencia-entre-cuentas-propias"),
    path('transferencia-terceros', transferencia_terceros_view, name="transferencia-terceros"),
    path('pagos', pagos_view, name="pagos"),
    path('solicitud-prestamo', prestamo_view, name="solicitud-prestamo"),
    path('pago-planillas', pago_planillas_view, name="pago-planillas"),
    path('pago-proveedores', pago_proveedores_view, name="pago-proveedores"),
    path('register', register_view, name="register"),
    path('login', login_view, name="login"),
    path('register-empresa', register_empresa_view, name="register-empresa"),
    path('admin/', admin.site.urls)
]
