from django.shortcuts import render
import requests


# Create your views here.


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
            r1 = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=151')
            ab = (r1.json()['results'])


            # Pokemon type Display
            r2 = requests.get('https://pokeapi.co/api/v2/pokemon/1')
            cd = (r2.json()['types'])


            # for x in range(1, 152):
            #     r2 = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(x))
            #     cd = (r2.json()['types'])
            #     pass
            # print(r2.json()['types'])



            data = False
        except:
            data = True
    return render(request, 'index.html', {'poke_type': poke_type, 'ab': ab, 'cd': cd,})