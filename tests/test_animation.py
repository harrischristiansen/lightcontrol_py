'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Test: Test Animations on Lights
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

import fuselights
LIGHT_ID = fuselights.bath_guest.lightID

animation = [
	AnimationStep(controls, LIGHT_ID, RED, tsTime=10),
	AnimationStep(controls, LIGHT_ID, BLUE, tsTime=10),
	AnimationStep(controls, LIGHT_ID, RED, tsTime=10),
	AnimationStep(controls, LIGHT_ID, BLUE, tsTime=10),
	AnimationStep(controls, LIGHT_ID, RED),
	AnimationStep(controls, LIGHT_ID, BLUE),
	AnimationStep(controls, LIGHT_ID, RED),
	AnimationStep(controls, LIGHT_ID, BLUE),
	AnimationStep(controls, LIGHT_ID, RED),
	AnimationStep(controls, LIGHT_ID, BLUE),
	AnimationStep(controls, LIGHT_ID, RED),
	AnimationStep(controls, LIGHT_ID, BLUE),
]

animation2 = [
	AnimationStep(controls, fuselights.window.lightID,	RED,	tsTime=2),
	AnimationStep(controls, fuselights.couch.lightID,	BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.mid.lightID,		RED,	tsTime=2),
	AnimationStep(controls, fuselights.tv.lightID,		BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.wall.lightID,	RED,	tsTime=2),
	AnimationStep(controls, fuselights.tvstand.lightID,	BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.fridge.lightID,	RED,	tsTime=2),
	AnimationStep(controls, fuselights.sink.lightID,	BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.oven.lightID,	RED,	tsTime=2),
	AnimationStep(controls, fuselights.bar.lightID,		BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.cabinet.lightID,	RED,	tsTime=2),
	AnimationStep(controls, fuselights.table.lightID,	BLUE,	tsTime=2, sTime=10),

	AnimationStep(controls, fuselights.window.lightID,	BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.couch.lightID,	RED,	tsTime=2),
	AnimationStep(controls, fuselights.mid.lightID,		BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.tv.lightID,		RED,	tsTime=2),
	AnimationStep(controls, fuselights.wall.lightID,	BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.tvstand.lightID,	RED,	tsTime=2),
	AnimationStep(controls, fuselights.fridge.lightID,	BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.sink.lightID,	RED,	tsTime=2),
	AnimationStep(controls, fuselights.oven.lightID,	BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.bar.lightID,		RED,	tsTime=2),
	AnimationStep(controls, fuselights.cabinet.lightID,	BLUE,	tsTime=2),
	AnimationStep(controls, fuselights.table.lightID,	RED,	tsTime=2),
]

def loopAnimation():
	for i in range(10):
		for step in animation:
			step.triggerStep()

if __name__ == '__main__':
	controls.startLightQueue()
	loopAnimation()
