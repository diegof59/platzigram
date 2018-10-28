"""
Platzigram views
"""

from django.http import HttpResponse
from datetime import datetime
import json


# Funciones vistas

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hola mundo, la fecha y hora son: {}'.format(now))


def sort(request):
    ##pdb : Debug
    # import pdb; pdb.set_trace()

    nums = request.GET['nums']

    nums_ordenada = ordenar(nums)

    data = {
        'Status': 200,
        'OrderedList': nums_ordenada,
        'Message': 'Success'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
    """
    #print(type(numsOrdenada))
    #return HttpResponse('Los numeros enviados son: '+ nums + '<br> Los numeros ordenados son: ' + str(numsOrdenada))
    
    #Retorna la lista convertida a JSON.
    #jsonSortedL = json.dumps(sortedList)
    #return HttpResponse(numsOrdenada, content_type='application/json')
    """


def greet(request, name, age):
    if age <= 12:
        answer = 'Disculpe,{}, no tiene la edad para ingresar.'.format(name)
    else:
        answer = 'Bienvenido(a), {} ;)'.format(name)

    return HttpResponse(answer)


# -------------------------
# Funciones auxiliares

# Recibe string, convierte en lista de int y la retorna ordenada.
def ordenar(argument):
    argument_list = argument.split(',')
    sorted_list = sorted(argument_list)

    return sorted_list
