from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class TailWindView(ListView):
    template_name = 'tailwind/pagina.html'

def tailwind_detail_view(request, **kwargs):
    productos = 'Holis Bolis'
    return render(request, 'tailwind/pagina.html', {'productos':productos})   