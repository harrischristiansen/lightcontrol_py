'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	HueControls: Package for controlling Philips Hue Lights
'''

import logging
import requests

class HueControls(object):

	def __init__(self, hueIPaddr, hueAPIKey):
		if len(hueIPaddr) < 8 or len(hueAPIKey) < 20:
			raise ValueError('Error: Hue IP Address and API Key are required')

		self.ipaddr = hueIPaddr
		self.apiKey = hueAPIKey
		self.baseUrl = 'http://' + self.ipaddr + '/api'
		self.baseAuthUrl = self.baseUrl + '/' + self.apiKey
		logging.debug("Connected to Hue Bridge!")

	def setLight(self, lightID, color, brightness=255, transitionTime=10):
		putRequest = requests.put(self.baseAuthUrl + '/lights/' + str(lightID) +'/state',
			data='{"bri": ' + str(brightness) + ', "transitiontime" : ' + str(transitionTime) + ', "hue": ' + str(color) +'}')
		return putRequest