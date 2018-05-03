'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Fuse Light Controller: Light controller for Fuse apartment
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

import fuselights

def setLightsBlue():
	controls.setAllLights(controls.hexToXY("#0000FF"))

def setLightsGreen():
	controls.setAllLights(controls.hexToXY("#00FF00"))

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	viewer = ControlsViewer("Hue Lights")
	viewer.setTitle("Hue Lights")
	viewer.setLights(fuselights.alllights)
	viewer.setAction(0, setLightsBlue)
	viewer.setAction(1, setLightsGreen)
	viewer.mainViewerLoop()
