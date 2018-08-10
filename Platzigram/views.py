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
    #import pdb; pdb.set_trace()
	
	nums = request.GET['nums']
	
	numsOrdenada = ordenar(nums)
	#print(type(numsOrdenada))
	#return HttpResponse('Los numeros enviados son: '+ nums + '<br> Los numeros ordenados son: ' + str(numsOrdenada))
	return HttpResponse(numsOrdenada, content_type='application/json')
	
def greet(request, name, age):
	if (age <= 12):
		answer = 'Disculpe,{}, no tiene la edad para ingresar.'.format(name)
	else:
		answer = 'Bienvenido(a), {} ;)'.format(name)
	
	return HttpResponse(answer)

	
	
# -------------------------
# Funciones auxiliares

def ordenar(argument):

	argumentList = argument.split(',')
	sortedList = sorted(argumentList)
	jsonSortedL = json.dumps(sortedList)
	return jsonSortedL