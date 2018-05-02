'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Step: Definition of step in an animation
'''

import logging
import time

class AnimationStep(object):
	def __init__(self, controls, lightID, color, tsTime=0, sTime=-1):
		self._controls = controls				# Light Control API
		self._lightID = lightID					# Light ID
		self._color = controls.hexToXY(color)	# Step Color
		self._tsTime = tsTime					# Transition Time
		self._sTime = sTime						# Sleep Time

		if self._sTime == -1:
			self._sTime = (self._tsTime/10)+.1

	def triggerStep(self, lightID=0):
		if lightID != 0:
			self._controls.setLight(lightID, self._color, transitionTime=self._tsTime)
		else:	
			self._controls.setLight(self._lightID, self._color, transitionTime=self._tsTime)
		time.sleep(self._sTime)