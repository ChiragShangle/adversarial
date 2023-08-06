from django.shortcuts import render

from django.http import HttpResponse


def evasion(request):
    model=None
    attack=None
    parameter=None
    range=None
    if request.method == 'POST':
        model = request.POST.get('model')
        attack = request.POST.get('attack')
    if model == 'DenseNet':
        if attack == 'FGSM':
            parameter= 'accuracy'
            range= '64 - 99%'    
    return render(request,"evasion.html",{'model':model , 'attack':attack, 'parameter':parameter, 'range':range})


def homepage(request):
    return render(request,"homepage.html")
def robustness(request):
    return render(request,"robustness.html")
