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
flashAnimation = FlashAnimation(lights, [ORANGE, RED, BLUE], numCycles=1, numFlashes=4)
twinkleAnimation = TwinkleFadeAnimation(lights, [ORANGE, BLUE, RED, ORANGE, PURPLE, GREEN], numCycles=2)
chaseAnimation = ChaseAnimation(lights, [PURPLE, RED, BLUE], numCycles=2, blockSize=7, moveDelay=0.8)
fadeToBlackAnimation = FadeToColorAnimation(fuselights.globalLight, [WHITE], brightness=1, tsTime=1)
fadeToColorAnimation = FadeToColorAnimation(fuselights.globalLight, [BLUE], brightness=200, tsTime=10)

if __name__ == '__main__':
	controls.startLightQueue()
	while True:
		twinkleAnimation.runAnimation()
		chaseAnimation.runAnimation()
	controls.stopLightQueue()
