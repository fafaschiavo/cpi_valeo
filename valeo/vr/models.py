from __future__ import unicode_literals

from django.db import models

# Create your models here.
class joystick(models.Model):
    joystick_data = models.CharField(max_length=200)
    angle = models.IntegerField(default=90)
    pedal = models.FloatField(default=0)
    left_buttons = models.IntegerField(default=0)
    right_buttons = models.IntegerField(default=0)

# state = joystick(joystick_data = '', angle = 90, pedal = 0, left_buttons = 0, right_buttons = 0)
# state.save()

# joystick.objects.get(id = 1)