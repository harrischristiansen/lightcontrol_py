'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	FadeToColorAnimation: Animation with fading to a specific color
'''

TS_TIME = 50

from .base.BaseAnimation import BaseAnimation

class FadeToColorAnimation(BaseAnimation):
	def __init__(self, lights=[], colors=[], numCycles=1, speed=1, brightness=255, tsTime=TS_TIME, sTime=None):
		self._brightness = brightness # Brightness
		self._tsTime = tsTime
		self._sTime = sTime
		super().__init__(lights, colors, numCycles, speed)

	def _generateAnimationSequence(self):
		self._sequence = []
		for light in self._lights:
			if light == self._lights[-1]:
				sTime = self._tsTime/6.5
				if self._sTime != None:
					sTime = self._sTime
				step = self.createStep(light, self._colors[0], bri=self._brightness, tsTime=self._tsTime, sTime=sTime)
			else:
				step = self.createStep(light, self._colors[0], bri=self._brightness, tsTime=self._tsTime, sTime=0)
			self._initialSequence.append(step)
