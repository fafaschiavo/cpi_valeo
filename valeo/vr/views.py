from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from vr.models import joystick
import json

def index(request):
    context = {}
    return render(request, 'index.html', context)

def index2(request):
    context = {}
    return render(request, 'index2.html', context)

def async_joystick(request):
	current_state = joystick.objects.get(id = 1)
	print 'current angle - ' + str(current_state.angle)
	print 'current pedal - ' + str(current_state.pedal)
	print 'current right_buttons - ' + str(current_state.right_buttons)
	print 'current left_buttons - ' + str(current_state.left_buttons)
	context = {}
	data_to_send = str(current_state.angle) + '&' + str(int(current_state.pedal))
	return HttpResponse(data_to_send)

@csrf_exempt
def receiver(request):
	#receive and decode data
	received_data = request.GET['data']
	encoded_data = json.loads(received_data)
	volant_angle = encoded_data['Volant']
	right_button_state = encoded_data['RightButton']
	left_button_state = encoded_data['LeftButton']
	pedal_state = encoded_data['Pedale']

	#Save in the database
	current_state = joystick.objects.get(id = 1)
	current_state.angle = volant_angle
	current_state.right_buttons = right_button_state
	current_state.left_buttons = left_button_state
	current_state.pedal = 100*float(pedal_state)
	current_state.save()

	context = {}
	return HttpResponse(200)

def concept(request):
    context = {}
    return render(request, 'concept.html', context)

def concept2(request):
    context = {}
    return render(request, 'concept2.html', context)

    # joystick_data = models.CharField(max_length=200)
    # angle = models.IntegerField(default=90)
    # pedal = models.FloatField(default=0)
    # left_buttons = models.IntegerField(default=0)
    # right_buttons = models.IntegerField(default=0)