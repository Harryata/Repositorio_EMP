from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, EditarPerfilForm
from django.contrib.auth import views as auth_views




# Registro de usuarios
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('perfil_usuario')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Vista del perfil
@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html')

# Edición del perfil
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})


#Azumy vuelve TwT