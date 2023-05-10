from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Count
from django.contrib import messages
from .models import Registro
from .forms import RegistroForm


# Vista de registros y total por ciudad
def registro_list(request):
    registro = Registro.objects.all()
    total_por_ciudad = Registro.objects.values('ciudad').annotate(total=Count('id'))
    context = {
        'registros': registro,
        'total_por_ciudad': total_por_ciudad
    }
    return render(request, 'registro_list.html', context)


# Crea un nuevo registro
def registro_create(request):
    form = RegistroForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Registro creado con éxito')
        return redirect('registro_list')
    return render(request, 'registro_form.html', {'form': form})


# Actualiza un registro existente
def registro_update(request, id):
    registro = get_object_or_404(Registro, id=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save()
            messages.success(request, 'Registro actualizado con éxito')
            return redirect('registro_list')
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'registro_form.html', {'form': form})


# Elimina un registro existente
def registro_delete(request, id):
    registro = get_object_or_404(Registro, id=id)
    registro.delete()
    messages.success(request, 'Registro eliminado con éxito')
    return redirect('registro_list')


# Muestra una lista de registros en formato JSON
def registro_list_json(request):
    registros = Registro.objects.all()
    data = [{'id': r.id, 'nombre': r.nombre, 'apellido': r.apellido, 'email': r.email} for r in registros]
    return JsonResponse({'data': data})


# Redirecciona a la lista de registros
def home(request):
    return redirect('registro_list')
