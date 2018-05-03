'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	TwinkleFadeAnimation: Animation with fading lights and random twinkles
'''

TS_TIME = 60
LOW_BRI = 90
HIGH_BRI = 240

from .BaseAnimation import BaseAnimation

class TwinkleFadeAnimation(BaseAnimation):
	def _generateAnimationSequence(self):
		if len(self._colors) < 2:
			raise ValueError("At least two colors must be provided")

		# Start with all lights color 1
		self._initialSequence = []
		for light in self._lights:
			step = self.createStep(light, self._colors[1], bri=LOW_BRI, tsTime=1)
			self._initialSequence.append(step)

		# Twinkle using color 0, and fade all other lights betwen remaining colors
		self._sequence = []

		loopCount = 1
		numFadeColors = len(self._colors) - 1
		for twinkleLight in self._lights:
			fadeToColor = self._colors[(loopCount%numFadeColors) + 1]

			step = self.createStep(twinkleLight, self._colors[0], bri=HIGH_BRI, tsTime=2) # Twinkle Selected Light
			self._sequence.append(step)

			for light in self._lights: # Fade All Lights
				step = self.createStep(light, fadeToColor, bri=LOW_BRI, tsTime=TS_TIME, sTime=.01)
				self._sequence.append(step)
			
			step = self.createStep(twinkleLight, fadeToColor, bri=LOW_BRI, tsTime=TS_TIME)
			self._sequence.append(step)

			loopCount += 1
