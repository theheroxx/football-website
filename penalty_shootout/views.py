from django.shortcuts import render

def penalty_shootout(request):
    return render(request, 'penalty_shootout/penalty_shootout.html')
