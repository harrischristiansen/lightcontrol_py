'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	TwinkleFadeAnimation: Animation with fading lights and random twinkles
'''

from .BaseAnimation import BaseAnimation

class TwinkleFadeAnimation(BaseAnimation):
	def _generateAnimationSequence(self):
		tsTime=10

		# Fade all lights between colors 0 and 1, and twinkle color 2
		self._sequence = []

		loopCount = 0
		for twinkleLight in self._lights:
			step = self.createStep(twinkleLight, self._colors[2], tsTime=2) # Twinkle Selected Light
			self._sequence.append(step)

			for light in self._lights: # Fade All Lights
				step = self.createStep(light, self._colors[loopCount%2], tsTime=tsTime, sTime=0)
				self._sequence.append(step)
			
			step = self.createStep(twinkleLight, self._colors[loopCount%2], tsTime=tsTime)
			self._sequence.append(step)

			loopCount += 1
