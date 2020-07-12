from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'main/index.html')

def Tramites(request):
    return render(request, 'main/tramites.html')

def Contacto(request):
    return render(request, 'main/contacto.html')
