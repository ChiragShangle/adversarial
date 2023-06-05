from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    model=None
    attack=None
    parameter=None
    if request.method == 'POST':
        model = request.POST.get('model')
        attack = request.POST.get('attack')
        parameter=request.POST.get('parameters')
    return render(request,"checkout.html",{'model':model , 'attack':attack, 'parameter':parameter})
# Create your views here.

# def fetch(request):
#  if request.method == 'POST':
#     model=request.POST.get('model')
        
