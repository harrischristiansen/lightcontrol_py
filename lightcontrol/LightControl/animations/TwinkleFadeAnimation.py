'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	TwinkleFadeAnimation: Animation with fading lights and random twinkles
'''

from .BaseAnimation import BaseAnimation

class TwinkleFadeAnimation(BaseAnimation):
	def _generateAnimationSequence(self):
		tsTime=60

		# Twinkle using color 0, and fade all other lights betwen remaining colors
		self._sequence = []

		loopCount = 0
		numFadeColors = len(self._colors) - 1
		for twinkleLight in self._lights:
			fadeToColor = self._colors[(loopCount%numFadeColors) + 1]

			step = self.createStep(twinkleLight, self._colors[0], tsTime=2) # Twinkle Selected Light
			self._sequence.append(step)

			for light in self._lights: # Fade All Lights
				step = self.createStep(light, fadeToColor, tsTime=tsTime, sTime=0)
				self._sequence.append(step)
			
			step = self.createStep(twinkleLight, fadeToColor, tsTime=tsTime)
			self._sequence.append(step)

			loopCount += 1
