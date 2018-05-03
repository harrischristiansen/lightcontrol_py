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
twinkleAnimation = TwinkleFadeAnimation(fuselights.mainroom, [ORANGE, BLUE, RED, PURPLE, GREEN], numCycles=4)
chaseAnimation = ChaseAnimation(fuselights.mainroom, [PURPLE, RED, BLUE], numCycles=3, blockSize=12, moveDelay=0.25)

if __name__ == '__main__':
	controls.startLightQueue()
	chaseAnimation.runAnimation()
	controls.stopLightQueue()
