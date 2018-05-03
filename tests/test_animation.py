'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Test: Test Animations on Lights
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

import fuselights
lights = [
	fuselights.wall.lightID,
	fuselights.window.lightID,
	fuselights.tv.lightID,
	fuselights.tvstand.lightID,
	fuselights.couch.lightID,
	fuselights.mid.lightID,
	fuselights.bar.lightID,
	fuselights.fridge.lightID,
	fuselights.oven.lightID,
	fuselights.sink.lightID,
	fuselights.cabinet.lightID,
]
animation = FlashAnimation(controls, lights, [WHITE, RED, BLUE], numCycles=2)

if __name__ == '__main__':
	controls.startLightQueue()
	animation.runAnimation()
	controls.stopLightQueue()
