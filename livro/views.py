from django.http import HttpResponse
from django.shortcuts import redirect, render
from usuarios.models import Usuario

from .models import Livros


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.all()
        return render(request, 'home.html', {'livros': livros})
    else:
        return redirect('/auth/login/?status=2')


