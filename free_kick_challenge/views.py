from django.shortcuts import render

def free_kick_challenge(request):
    return render(request, 'free_kick_challenge/free_kick_challenge.html')
