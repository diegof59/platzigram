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
	
	aux(nums)
	
	return HttpResponse('Los numeros enviados son: ' + nums)
	
def aux(argument):

	argumentList = argument.split(',')
	#print(type(argumentList))
	print(argumentList)