from django.shortcuts import render

from django.http import HttpResponse


def evasion(request):
    model=None
    attack=None
    parameter=None
    if request.method == 'POST':
        model = request.POST.get('model')
        attack = request.POST.get('attack')
        parameter=request.POST.get('parameters')
    return render(request,"evasion.html",{'model':model , 'attack':attack, 'parameter':parameter})


def homepage(request):
    return render(request,"homepage.html")
def robustness(request):
    return render(request,"robustness.html")
