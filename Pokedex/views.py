from django.shortcuts import render
import requests


def index(request):
    data = True
    result = None
    poke_type = None
    r1 = None
    ab = None
    cd = None
    r2 = None
    while (data):
        try:
            result = requests.get('https://pokeapi.co/api/v2/type/')
            json = result.json()
            poke_type = (json['results'])



            data = False
        except:
            data = True

    return render(request, 'index.html', {'poke_type': poke_type, 'ab': ab, 'cd': cd,})