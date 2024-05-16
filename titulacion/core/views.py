from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def pagina(request):
    return render(request, 'pagina.html')

def detalles(request):
    return render(request, 'detalles.html')

def login(request):
    return render(request, 'login.html')



from django.shortcuts import render
from . forms import UsuarioForm

def formulario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form': form})