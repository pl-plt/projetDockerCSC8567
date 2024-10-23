from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
#    return HttpResponse("Hello, World!")
    return render(request, 'home.html')

def formulaireNom(request):
    return render(request, 'formulaireNom.html')

def success(request):
    return render(request, 'success.html')