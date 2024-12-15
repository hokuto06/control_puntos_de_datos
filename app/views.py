from django.shortcuts import render, get_object_or_404, redirect
from .models import Punto
from .forms import PuntoForm

def punto_list(request):
    if request.method == 'POST':
        form = PuntoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('punto_list')
    else:
        form = PuntoForm()

    puntos = Punto.objects.all()
    return render(request, 'app/punto_list.html', {'form': form, 'puntos': puntos})

def delete_punto(request, pk):
    punto = get_object_or_404(Punto, pk=pk)
    punto.delete()
    return redirect('punto_list')

def punto_detail(request, pk):
    punto = get_object_or_404(Punto, pk=pk)
    return render(request, 'app/punto_detail.html', {'punto': punto})
