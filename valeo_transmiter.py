import pygame
import time
import requests
import urllib

pygame.display.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
#print joysticks[0]

joysticks[0].init()

#print 'Get name'
#print joysticks[0].get_name()
#
#print 'Get number of axis'
#print joysticks[0].get_numaxes()
amount_of_axis = joysticks[0].get_numaxes()

#print 'Get number of balls'
#print joysticks[0].get_numballs()
#
#print 'Get number of buttons'
#print joysticks[0].get_numbuttons()
#
#print 'Get number of hats'
#print joysticks[0].get_numhats()

#PARAMETRES CALIBRATION (MIN ET MAX)
y2=180
y1=0
x2=1.999969482421875
x1=0
facteur1=(y2-y1)/(x2-x1)
b2=1
b1=0
a2=0.835296630859375
a1=0.003936767578125
facteur2=(b2-b1)/(a2-a1)

#FONCTION DE CALIBRATION DES AXES
def rescale(valeur,number):
	rescaled = 0
	if(number==0):
		rescaled = int((valeur+1-x1)*facteur1+y1)
	else:
		if(valeur>0):
			rescaled=0
		else:
			valeur = -valeur
			rescaled = ((valeur-a1)*facteur2+b1)
	return rescaled;

#AGGREGATE LEFT BUTTON AND RIGHT BUTTON
def getbuttons(number):
	sum=0
	if(number==1):
		sum=joysticks[0].get_button(0)+joysticks[0].get_button(1)+joysticks[0].get_button(2)+joysticks[0].get_button(3)+joysticks[0].get_button(4)+joysticks[0].get_button(6)+joysticks[0].get_button(9)+joysticks[0].get_button(10)
		if(sum!=0):
			return 1;
		else:
			return 0;
	else:
		sum=joysticks[0].get_button(5)+joysticks[0].get_button(7)+joysticks[0].get_button(8)+joysticks[0].get_button(11)
		if(sum!=0):
			return 1;
		else:
			if(joysticks[0].get_hat(0)==(0,0)):
				return 0;
			else:
				return 1;

#BOUCLE
while True:
	pygame.event.pump()
	# axis_position = joysticks[0].get_axis(1)
	data_to_transmit = '{"Volant" : "'+ str(rescale(joysticks[0].get_axis(0),0))+'", "Pedale" : "'+ str(rescale(joysticks[0].get_axis(1),1))+'", "LeftButton" : "'+str(getbuttons(0))+'", "RightButton" : "'+ str(getbuttons(1))+'"}'
	print data_to_transmit
	print '--------------------------------'
	
	url = 'http://127.0.0.1:8000/vr/receiver/'

	params = {'data': data_to_transmit}

	# requests.post(url, params=params, json=data)
	requests.get(url, params=urllib.urlencode(params))

	time.sleep(0.1)





