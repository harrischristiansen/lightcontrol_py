'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Fuse Light Controller: Light controller for Fuse apartment
'''

import logging
logging.basicConfig(level=logging.DEBUG)

from HueControls import HueControls
import time

import fuselights

HUE_BRIDGE_IP = '10.3.0.177'
HUE_BRIDGE_API_KEY = 'd5orxbetHKF46FCV1wBmnFTVNSkGQWMSjwNOHu2i'

controls = HueControls(HUE_BRIDGE_IP, HUE_BRIDGE_API_KEY)

def setLightBlue(tsTime=50):
	controls.setLight(fuselights.bath_guest.lightID, controls.hexToXY("#0000FF"), transitionTime=tsTime)

def setLightGreen(tsTime=50):
	controls.setLight(fuselights.bath_guest.lightID, controls.hexToXY("#00FF00"), transitionTime=tsTime)

def setLightRed(tsTime=50):
	controls.setLight(fuselights.bath_guest.lightID, controls.hexToXY("#FF0000"), transitionTime=tsTime)

def loopColors(i):
	setLightBlue(int(i/2)+1)
	time.sleep(i*.05)
	setLightGreen(int(i/2)+1)
	time.sleep(i*.05)
	setLightRed(int(i/2)+1)
	time.sleep(i*.05)

def loopColorsFixed(tsTime=0, sTime=0.3):
	setLightBlue(tsTime)
	time.sleep(sTime)
	setLightGreen(tsTime)
	time.sleep(sTime)
	setLightRed(tsTime)
	time.sleep(sTime)

if __name__ == '__main__':
	for i in range(100):
		loopColorsFixed()