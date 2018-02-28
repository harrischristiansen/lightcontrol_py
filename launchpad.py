'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Controls: Basic test lighting controls
'''

HUE_BRIDGE_IP = '10.3.0.177'
HUE_BRIDGE_API_KEY = 'd5orxbetHKF46FCV1wBmnFTVNSkGQWMSjwNOHu2i'

from HueControls import HueControls
import launchpad_py
import logging
import time

LP_RED = 5
LP_GREEN = 21
LP_BLUE = 79
LP_WHITE = 3

controls = None
lp = None

def bootupSeq():
	for i in [LP_RED, LP_GREEN, LP_BLUE, LP_WHITE]:
		if i != LP_RED:
			time.sleep(0.5)
		lp.LedAllOn(i)

def init():
	global lp
	controls = HueControls(HUE_BRIDGE_IP, HUE_BRIDGE_API_KEY)
	controls.setAllLights(controls.hexToXY("#FF0000"))

	lp = launchpad_py.LaunchpadPro()

	if lp.Open(0, "pro"):
		logging.debug("Launchpad Connected")
	else:
		raise ValueError('Error: Launchpad Not Found')

	bootupSeq()

def close():
	lp.Reset()
	lp.Close()

def setColorpad():
	lp.LedCtrlXY(0, 1, 255, 0, 0)
	lp.LedCtrlXY(0, 2, 0, 255, 0)
	lp.LedCtrlXY(0, 3, 0, 0, 255)

lastCoord = (0, 0)
def checkUserSequence():
	global lastCoord
	lp.ButtonFlush()
	while True:
		state = lp.ButtonStateXY()
		if state:
			x, y, pressed = state
			if lastCoord != (x, y):
				lastCoord = (x, y)
				return False
			print("pushed coord: (%s, %s, %s)" % (x, y, pressed))
			lp.LedAllOn(LP_WHITE)
			setColorpad()

def main():
	setColorpad()
	while True:
		checkUserSequence()

if __name__ == "__main__":
	init()
	try:
		main()
	except KeyboardInterrupt as ki:
		logging.debug("Interrupted - Exiting...")
	close()