'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Launchpad: Lighting Controller using Novation Launchpad
'''

HUE_BRIDGE_IP = '10.3.0.177'
HUE_BRIDGE_API_KEY = 'd5orxbetHKF46FCV1wBmnFTVNSkGQWMSjwNOHu2i'

from HueControls import HueControls
import launchpad_py
import logging
import time

from lppro_colorcodes import *
from colormap import colormap

controls = None
lp = None

def bootupSeq():
	for i in [LP_RED, LP_GREEN, LP_BLUE, LP_WHITE]:
		if i != LP_RED:
			time.sleep(0.4)
		lp.LedAllOn(i)

def init():
	global lp, controls
	controls = HueControls(HUE_BRIDGE_IP, HUE_BRIDGE_API_KEY)
	#controls.setAllLights(controls.hexToXY("#FF0000"))

	lp = launchpad_py.LaunchpadPro()

	if lp.Open(0, "pro"):
		logging.debug("Launchpad Connected")
	else:
		raise ValueError('Error: Launchpad Not Found')

	bootupSeq()

def close():
	lp.Reset()
	lp.Close()

def colorFor(x, y):
	index = x*8 + (y-1)
	if index < len(colormap):
		return colormap[index]
	return (255, 255, 255)

def colorWithCoord(x, y):
	color = colorFor(x, y)
	return (x, y) + color

def setColorpad():
	lp.LedCtrlXY(*colorWithCoord(0, 1))
	lp.LedCtrlXY(*colorWithCoord(0, 2))
	lp.LedCtrlXY(*colorWithCoord(0, 3))

def checkUserSequence():
	lp.ButtonFlush()
	while True:
		state = lp.ButtonStateXY()
		if state:
			x, y, pressed = state
			if pressed != 0:
				logging.debug("Pressed button: (%s, %s, %s)" % (x, y, pressed))
				controls.setAllLights(controls.rgbToXY(*colorFor(x,y)), transitionTime=2)
				lp.LedCtrlXY(x, y, 255, 255, 0)
			else:
				lp.LedCtrlXY(*colorWithCoord(x, y))

def main():
	setColorpad()
	while True:
		checkUserSequence()

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	init()
	try:
		main()
	except KeyboardInterrupt as ki:
		logging.debug("Interrupted - Exiting...")
	close()