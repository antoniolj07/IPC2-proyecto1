from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hellow world</h1>')  # string of HTML code
    return render(request, 'home/home.html', {})

def nueva_cuenta_view(request, *args, **kwargs):
    return render(request, 'home/crear-cuenta.html', {})

def estado_cuenta_view(request, *args, **kwargs):
    return render(request, 'home/estado-cuenta.html', {})

def cuentas_propias_view(request, *args, **kwargs):
    return render(request, 'home/transferencia-propias.html', {})

def transferencia_terceros_view(request, *args, **kwargs):
    return render(request, 'home/transferencia-terceros.html', {})

def pagos_view(request, *args, **kwargs):
    return render(request, 'home/pagos.html', {})

def prestamo_view(request, *args, **kwargs):
    return render(request, 'home/solicitud-prestamo.html', {})

def cuentas_view(request, *args, **kwargs):
    return render(request, 'home/cuentas.html', {})

def pago_planillas_view(request, *args, **kwargs):
    return render(request, 'home/pagar-planillas.html', {})

def pago_proveedores_view(request, *args, **kwargs):
    return render(request, 'home/pago-proveedores.html', {})

def about_view(request, *args, **kwargs):
    # return HttpResponse('<h1>About Page</h1>')
    my_context = {
        'my_text': 'this is about me',
        'number': 123,
        'my_list': ['jorge', 'antoino', 'perez', 'ordo;ez', 'fin'],
        'boolin': True
    }
    return render(request, 'about.html', my_context)