'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	HueControls: Package for controlling Philips Hue Lights
'''

import logging
import time

class HueControls(object):

	def __init__(self, hueIPaddr, hueAPIKey):
		if len(hueIPaddr) < 11 or len(hueAPIKey) < 20:
			raise ValueError('Error: Hue IP Address and API Key are required')

		self.ipaddr = hueIPaddr
		self.apiKey = hueAPIKey
		logging.debug("Connected to Hue Bridge!")

	def testMethod(self):
		print("Test!")