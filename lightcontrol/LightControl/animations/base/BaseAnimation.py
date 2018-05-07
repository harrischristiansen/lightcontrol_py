'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	BaseAnimation: Base Animation Class
'''

from LightControl import AnimationStep, Light

class BaseAnimation(object):
	def __init__(self, lights=[], colors=[], numCycles=1, speed=1):
		if (not isinstance(lights, list)) or (not isinstance(lights[0], Light)):
			raise ValueError("lights must be a list of Light Objects")

		self._lights = lights								# List of lights for animation
		self._lightsLen = len(lights)						# Count of lights for animation
		self._colors = colors								# List of colors for animation
		self._numCycles = sorted((1, numCycles, 100))[1]	# Number of cycles to loop animation
		self._speed = sorted((0, speed, 1000))[1]			# Render speed for animation

		self._running = True
		self._initialSequence = []
		self._sequence = []
		self._generateAnimationSequence()

	def run(self):
		self._running = True
		for step in self._initialSequence:
			step.triggerStep()
			if not self._running:
				return False
		for i in range(self._numCycles):
			for step in self._sequence:
				step.triggerStep()
				if not self._running:
					return False

	def stop(self):
		self._running = False

	def createStep(self, light, color, bri=255, tsTime=0, sTime=-1):
		tsTime *= self._speed
		if sTime > 0:
			sTime *= self._speed
		return AnimationStep(light, color, bri=bri, tsTime=tsTime, sTime=sTime)

	def _generateAnimationSequence(self):
		self._initialSequence = []
		self._sequence = []
