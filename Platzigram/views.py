"""
Platzigram views
"""

from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hola mundo, la fecha y hora son: {}'.format(now))

def some_funct(request):
    #pdb : Debug
    #import pdb; pdb.set_trace()
	
	nums = request.GET['nums']
	
	numsOrdenada = ordenar(nums)
	
	return HttpResponse('Los numeros enviados son: '+ nums + '<br> Los numeros ordenados son: ' + str(numsOrdenada))
	
def ordenar(argument):

	argumentList = argument.split(',')
	sortedList = sorted(argumentList)
	return sortedList