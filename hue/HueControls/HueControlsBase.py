'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	HueControls: Package for controlling Philips Hue Lights
'''

import json
import logging
import requests

class HueControlsBase(object):
	def __init__(self, hueIPaddr, hueAPIKey):
		if len(hueIPaddr) < 8 or len(hueAPIKey) < 20:
			raise ValueError('Error: Hue IP Address and API Key are required')

		self._ipaddr = hueIPaddr
		self._apiKey = hueAPIKey
		self._baseURL = 'http://' + self._ipaddr + '/api'
		self._baseAuthURL = self._baseURL + '/' + self._apiKey

		self._lights = self._lightIDs = {}
		self._lightCount = 0
		self._loadLights()

	# Request URLs

	def _getLightsURL(self):
		return self._baseAuthURL + '/lights/'

	def _getLightQueryURL(self, lightID):
		return self._getLightsURL() + str(lightID)

	def _getLightPutURL(self, lightID):
		return self._getLightQueryURL(lightID) +'/state'

	def _getGroupActionPutURL(self, groupID):
		return self._baseAuthURL + '/groups/' + str(groupID) +'/action'

	# Get Requests

	def _getLightRequest(self, lightID):
		light = requests.get(self._getLightQueryURL(lightID))
		if light.status_code == 200:
			return light.json()
		return {}

	def _loadLights(self):
		lights = requests.get(self._getLightsURL())
		if lights.status_code != 200:
			raise ValueError('Error: Invalid Hue IP Address or API Key - connection failed')
		self._lights = lights.json()
		self._lightIDs = list(self._lights.keys())
		self._lightCount = len(self._lights)
		logging.debug("Connected to Hue Bridge!")

	# Put Requests

	def _buildRequest(self, brightness=None, transitionTime=None, xyColor=None, hue=None):
		request = {}
		if brightness:
			request['bri'] = int(brightness)
		if transitionTime != None:
			request['transitiontime'] = int(transitionTime)
		if xyColor:
			request['xy'] = xyColor
		if hue:
			request['hue'] = int(hue)
		return json.dumps(request)

	def _putLightRequest(self, lightID, data):
		return requests.put(self._getLightPutURL(lightID), data=data)

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	filename = __file__[__file__.rfind('/')+1:]
	logging.debug("%s called on it's own, performing self test" % filename)
	base = HueControlsBase("0.0.0.0", "abcdefghijklmnopqrstuvwxyz")