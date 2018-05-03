'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	FadeToColorAnimation: Animation with fading to a specific color
'''

TS_TIME = 50

from .BaseAnimation import BaseAnimation

class FadeToColorAnimation(BaseAnimation):
	def __init__(self, lights=[], colors=[], numCycles=1, speed=1, brightness=255, tsTime=TS_TIME):
		self._brightness = brightness # Brightness
		self._tsTime = tsTime
		super().__init__(lights, colors, numCycles, speed)

	def _generateAnimationSequence(self):
		self._sequence = []
		for light in self._lights:
			if light == self._lights[-1]:
				sTime = self._tsTime/6.5
				step = self.createStep(light, self._colors[0], bri=self._brightness, tsTime=self._tsTime, sTime=sTime)
			else:
				step = self.createStep(light, self._colors[0], bri=self._brightness, tsTime=self._tsTime, sTime=0)
			self._initialSequence.append(step)
