from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def pagina(request):
    return render(request, 'pagina.html')

def detalles(request):
    return render(request, 'detalles.html')



