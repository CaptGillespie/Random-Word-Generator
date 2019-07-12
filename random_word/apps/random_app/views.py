from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def random(request):
    gibberish = get_random_string(length=14)
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    context= {
        "gibberish":gibberish,
        "attempt": request.session["counter"]
    }
    return render(request,'random_app/index.html', context, request.session)
    
def generate(request):
    return redirect ('/', request.session)