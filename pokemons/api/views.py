import json

import urllib3
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

"""
def pokemonList(request):

    url = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=6'
    http = urllib3.PoolManager()
    jsonData = json.loads(http.request('GET', url).data)
    print(jsonData)
    pokemoncount = len(jsonData['results'])
    data = []
    for i in range(pokemoncount):
        pokemonURL = (jsonData['results'][i]['url'])
        data.append((json.loads(http.request('GET', pokemonURL).data)))
    pokemonList = {
        'pokemonList': data,
    }
    return render(request, 'pokemon-list.html', pokemonList)
"""

def list(request):
    if request.method=='POST':
        nextURL = request.POST['nextURL']
        http = urllib3.PoolManager()
        jsonData = json.loads(http.request('GET', nextURL).data)
        nextURL = jsonData['next']
        pokemoncount = len(jsonData['results'])
        data = []
        for i in range(pokemoncount):
            pokemonURL = (jsonData['results'][i]['url'])
            data.append((json.loads(http.request('GET', pokemonURL).data)))
        pokemonList = {
            'pokemonList': data,
            'nextURL': nextURL,
        }
        return render(request, 'pokemon-list.html', pokemonList)

    else:
        url = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=6'
        http = urllib3.PoolManager()
        jsonData = json.loads(http.request('GET', url).data)
        nextURL = jsonData['next']
        print(nextURL)
        pokemoncount = len(jsonData['results'])
        data = []
        for i in range(pokemoncount):
            pokemonURL = (jsonData['results'][i]['url'])
            data.append((json.loads(http.request('GET', pokemonURL).data)))
        pokemonList = {
            'pokemonList': data,
            'nextURL':nextURL,
        }
        return render(request, 'pokemon-list.html', pokemonList)


