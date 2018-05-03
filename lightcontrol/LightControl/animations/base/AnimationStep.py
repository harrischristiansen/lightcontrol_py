'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Step: Definition of step in an animation
'''

import time

class AnimationStep(object):
	def __init__(self, light, color, bri=255, tsTime=0, sTime=-1):
		self._light = light							# Light Object
		self._brightness = sorted((0, bri, 255))[1]	# Step Brightness
		self._color = color							# Step Color
		self._tsTime = tsTime						# Transition Time
		self._sTime = sTime							# Sleep Time

		if self._sTime == -1:
			self._sTime = (self._tsTime/10)+.13

	def __repr__(self):
		return "Light [%s] -> %s over %d ms" % (self._light.lightName, self._color, self._tsTime*100)

	def triggerStep(self):
		self._light.setLight(self._color, brightness=self._brightness, tsTime=self._tsTime)
		time.sleep(self._sTime)