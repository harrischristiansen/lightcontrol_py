'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Test: Test Animations on Single Light
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

import fuselights
LIGHT_ID = 6 #fuselights.bath_guest.lightID

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

def loopAnimation():
	for step in animation:
		step.triggerStep()

if __name__ == '__main__':
	for i in range(10):
		loopAnimation()