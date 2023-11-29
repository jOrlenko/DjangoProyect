from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            sendemail = EmailMessage('Mensaje desde AppDjango', f'El usario {nombre} desde la direecion {email} escribe:\n {contenido}', 'jorlenko.dev@gmail.com')
            
            try:
                sendemail.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?invalido')
    return render(request, 'contacto/contacto.html', {'elformulario':formulario_contacto})