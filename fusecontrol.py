'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Fuse Light Controller: Light controller for Fuse apartment
'''

from HueControls import HueControls
import logging

import fuselights
from viewer.viewer import ControlsViewer

HUE_BRIDGE_IP = '10.3.0.177'
HUE_BRIDGE_API_KEY = 'd5orxbetHKF46FCV1wBmnFTVNSkGQWMSjwNOHu2i'

controls = HueControls(HUE_BRIDGE_IP, HUE_BRIDGE_API_KEY)

def setLightsBlue():
	controls.setAllLights(controls.hexToXY("#0000FF"))

def setLightsGreen():
	controls.setAllLights(controls.hexToXY("#00FF00"))

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	viewer = ControlsViewer("Hue Lights")
	viewer.setTitle("Hue Lights")
	viewer.setLights(fuselights.lights)
	viewer.setAction(0, setLightsBlue)
	viewer.setAction(1, setLightsGreen)
	viewer.mainViewerLoop()
