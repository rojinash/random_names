from django.shortcuts import render, HttpResponse, redirect
import random
import math
# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    if request.session['count'] == 11 or request.session['count'] == 12 or request.session['count'] == 13:
        suffix = 'th'
    else:
        last_digit = request.session['count'] % 10
        if(last_digit == 1):
            suffix = 'st'
        elif(last_digit == 2):
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    names = ['Nick', 'Frances', 'Greg', 'Geo', 'Ashton', 'Erika', 'Houtan', 'Keoni', 'Baxter']
    index = round(random.random()*len(names)) - 1
    context = {
        'name': names[index],
        'count': request.session['count'],
        'suffix': suffix
    }
    return render(request, 'index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')
