'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	BaseAnimation: Base Animation Class
'''

import logging

if __name__ == '__main__':
	from AnimationStep import AnimationStep
else:
	from .AnimationStep import AnimationStep

class BaseAnimation(object):
	def __init__(self, controls, lights=[], colors=[], numCycles=1, speed=1):
		self._controls = controls							# Light Control API
		self._lights = lights								# List of lights for animation
		self._lightsLen = len(lights)						# Count of lights for animation
		self._colors = colors								# List of colors for animation
		self._numCycles = sorted((1, numCycles, 100))[1]	# Number of cycles to loop animation
		self._speed = sorted((0, speed, 10))[1]				# Render speed for animation

		self._initialSequence = []
		self._sequence = []
		self._generateAnimationSequence()

	def runAnimation(self):
		for step in self._initialSequence:
			step.triggerStep()
		for i in range(self._numCycles):
			for step in self._sequence:
				step.triggerStep()

	def createStep(self, lightID, color, tsTime=0, sTime=-1):
		return AnimationStep(self._controls, lightID, color, tsTime, sTime)

	def _generateAnimationSequence(self):
		self._initialSequence = []
		self._sequence = []
