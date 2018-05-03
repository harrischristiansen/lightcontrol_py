'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Test: Test Animations on Lights
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

import fuselights
flashAnimation = FlashAnimation(fuselights.mainroom, [WHITE, RED, BLUE], numCycles=2, numFlashes=3)
twinkleAnimation = TwinkleFadeAnimation(fuselights.mainroom, [ORANGE, BLUE, RED, PURPLE, GREEN], numCycles=2)

if __name__ == '__main__':
	controls.startLightQueue()
	flashAnimation.runAnimation()
	#twinkleAnimation.runAnimation()
	controls.stopLightQueue()
