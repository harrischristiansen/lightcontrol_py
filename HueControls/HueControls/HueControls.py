'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	HueControls: Package for controlling Philips Hue Lights
'''

import rgbxy

from .HueControlsBase import HueControlsBase

class HueControls(HueControlsBase):
	def __init__(self, hueIPaddr, hueAPIKey):
		HueControlsBase.__init__(self,hueIPaddr, hueAPIKey)
		self.converter = rgbxy.Converter()

	# Colors

	def hexToXY(self, hexVal):
		if hexVal[0] == '#':
			hexVal = hexVal[1:]
		return list(self.converter.hex_to_xy(hexVal))

	def rgbToXY(self, red, green, blue):
		return list(self.converter.rgb_to_xy(red, green, blue))

	def XYToHex(self, x, y, bri):
		return self.converter.xy_to_hex(x, y, bri)

	# Get Requests

	def getLight(self, lightID):
		return self._getLightRequest(lightID)

	def getBrightness(self, lightID):
		return 0

	def getColor(self, lightID):
		return 0

	# Put Requests

	def setLight(self, lightID, xyColor, brightness=255, transitionTime=5):
		data = self.buildRequest(brightness, transitionTime, xyColor)
		return self._putLightRequest(lightID, data)

	def setLightHue(self, lightID, hue, brightness=255, transitionTime=5):
		data = self.buildRequest(brightness, transitionTime, hue=hue)
		return self._putLightRequest(lightID, data)

	def setAllLights(self, xyColor, brightness=255, transitionTime=5):
		data = self.buildRequest(brightness, transitionTime, xyColor)
		for lightID in self._lightIDs:
			self._putLightRequest(lightID, data)
		return True
