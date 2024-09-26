from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'RecycLocator/index.html')
def mapa(request):
    return render(request, 'RecycLocator/mapa.html')