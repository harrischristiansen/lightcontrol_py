'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	FlashAnimation: Animation with Flashing Lights
'''

LOW_BRI = 90
HIGH_BRI = 200

from .base.BaseAnimation import BaseAnimation

class FlashAnimation(BaseAnimation):
	def __init__(self, lights=[], colors=[], numCycles=1, speed=1, numFlashes=4):
		self._numFlashes = numFlashes
		super(FlashAnimation, self).__init__(lights, colors, numCycles, speed)

	def _generateAnimationSequence(self):
		# Start with all lights color 0
		self._initialSequence = []
		for light in self._lights:
			step = self.createStep(light, self._colors[0], bri=LOW_BRI, tsTime=100, sTime=0.02)
			self._initialSequence.append(step)

		# Randomly strobe each light using colors 1 and 2, reset to 0
		self._sequence = []
		for light in self._lights:
			for c in range(self._numFlashes):
				step = self.createStep(light, self._colors[1], bri=HIGH_BRI, tsTime=0)
				self._sequence.append(step)
				step = self.createStep(light, self._colors[2], bri=HIGH_BRI, tsTime=0)
				self._sequence.append(step)
			step = self.createStep(light, self._colors[0], bri=LOW_BRI, tsTime=90, sTime=0)
			self._sequence.append(step)
