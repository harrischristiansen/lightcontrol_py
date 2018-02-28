'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	HueControls: Package for controlling Philips Hue Lights
'''

from .HueControlsBase import HueControlsBase

class HueControls(HueControlsBase):
	def __init__(self, hueIPaddr, hueAPIKey):
		HueControlsBase.__init__(self,hueIPaddr, hueAPIKey)

	# Get Requests

	def getLight(self, lightID):
		return self._getLightRequest(lightID)

	def getBrightness(self, lightID):
		return 0

	def getColor(self, lightID):
		return 0

	# Put Requests

	def setLight(self, lightID, color, brightness=255, transitionTime=5):
		data = '{"bri": ' + str(brightness) + ', "transitiontime" : ' + str(transitionTime) + ', "hue": ' + str(color) +'}'
		return self._putLightRequest(lightID, data)

	def setAllLights(self, color, brightness=255, transitionTime=5):
		data = '{"bri": ' + str(brightness) + ', "transitiontime" : ' + str(transitionTime) + ', "hue": ' + str(color) +'}'
		for lightID in self._lightIDs:
			self._putLightRequest(lightID, data)
		return True
