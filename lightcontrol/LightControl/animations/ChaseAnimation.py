'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	ChaseAnimation: Animation with chasing lights of specified block size
'''

LOW_BRI = 60
HIGH_BRI = 240

from .BaseAnimation import BaseAnimation

class ChaseAnimation(BaseAnimation):
	def __init__(self, lights=[], colors=[], numCycles=1, speed=1, blockSize=1, moveDelay=0.5):
		self._blockSize = blockSize
		self._moveDelay = moveDelay
		super(ChaseAnimation, self).__init__(lights, colors, numCycles, speed)

	def _generateAnimationSequence(self):
		# Iterate through lights with colors in groups of blockSize
		self._sequence = []
		nColors = len(self._colors)

		for c in range(self._blockSize*nColors):
			i = 0
			for light in self._lights:
				lColor = self._colors[int((i+c)/self._blockSize) % nColors]
				i += 1

				if (i+c-1) % self._blockSize == 0:
					step = self.createStep(light, lColor, bri=HIGH_BRI, tsTime=1, sTime=0.05)
					self._sequence.append(step)

					tsTime = int(self._moveDelay*10)*self._blockSize+2
					if i >= self._lightsLen-self._blockSize:
						step = self.createStep(light, lColor, bri=LOW_BRI, tsTime=tsTime, sTime=self._moveDelay)
					else:
						step = self.createStep(light, lColor, bri=LOW_BRI, tsTime=tsTime, sTime=0.05)
					self._sequence.append(step)
