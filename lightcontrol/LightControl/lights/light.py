'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Light: Model for Light Instance
'''

import logging

class Light(object):
	def __init__(self, controls, lightID, lightName, x, y):
		# Public Properties
		self.lightID = lightID		# Light ID
		self.lightName = lightName	# Light Name
		self.x = x					# % X coordinate for light on 2D map (0 <= x <= 1)
		self.y = y					# % Y coordinate for light on 2D map (0 <= y <= 1)

		# Private Properties
		self._controls = controls

	def __repr__(self):
		return "%s (%d): (%f, %f)" % (self.lightName, self.lightID, self.x, self.y)

	def setLight(self, xyColor, brightness=255, tsTime=5):
		self._controls.setLight(self.lightID, xyColor, brightness=brightness, transitionTime=tsTime)

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	logging.debug("Light called on it's own, performing self test")
	light = Light(None, 2, "Light Name", 0.2, 0.3)
	print(light)