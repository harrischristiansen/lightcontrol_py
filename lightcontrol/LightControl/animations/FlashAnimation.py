'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	FlashAnimation: Animation with Flashing Lights
'''

if __name__ == '__main__':
	from BaseAnimation import BaseAnimation
else:
	from .BaseAnimation import BaseAnimation

class FlashAnimation(BaseAnimation):
	def _generateAnimationSequence(self):
		self._sequence = []

		# Start with all lights color 0
		for light in self._lights:
			step = self.createStep(light, self._colors[0], tsTime=0)
			self._sequence.append(step)

		# Randomly strobe each light using colors 1 and 2, reset to 0
		for light in self._lights:
			for c in range(4):
				step = self.createStep(light, self._colors[1], tsTime=0)
				self._sequence.append(step)
				step = self.createStep(light, self._colors[2], tsTime=0)
				self._sequence.append(step)
			step = self.createStep(light, self._colors[0], tsTime=2, sTime=0)
			self._sequence.append(step)
