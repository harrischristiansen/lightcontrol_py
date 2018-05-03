'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Animation Test: Test Animations on Lights
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

import fuselights
lights = fuselights.mainroom
flashAnimation = FlashAnimation(lights, [YELLOW, RED, BLUE], numCycles=1, numFlashes=3)
twinkleAnimation = TwinkleFadeAnimation(lights, [ORANGE, BLUE, RED, PURPLE, GREEN], numCycles=1)
chaseAnimation = ChaseAnimation(lights, [PURPLE, RED, BLUE], numCycles=2, blockSize=len(lights), moveDelay=0.3)

if __name__ == '__main__':
	controls.startLightQueue()
	while True:
		chaseAnimation.runAnimation()
		flashAnimation.runAnimation()
		twinkleAnimation.runAnimation()
		flashAnimation.runAnimation()
	controls.stopLightQueue()
