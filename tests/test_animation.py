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
l1			= Light(controls, 3, "TV", 0.5, 0.7)
l2			= Light(controls, 5, "TV", 0.5, 0.7)
lights = [l1, l2]
flashAnimation = FlashAnimation(lights, [ORANGE, RED, BLUE], numCycles=20, numFlashes=4)
twinkleAnimation = TwinkleFadeAnimation(lights, [ORANGE, BLUE, RED, ORANGE, PURPLE, GREEN], numCycles=2)
chaseAnimation = ChaseAnimation(lights, [PURPLE, GREEN, BLUE], numCycles=2, blockSize=6, moveDelay=0.2)
fadeToBlackAnimation = FadeToColorAnimation(fuselights.globalLight, [WHITE], brightness=1, tsTime=1)
fadeToColorAnimation = FadeToColorAnimation(fuselights.globalLight, [BLUE], brightness=200, tsTime=10)

ceilingAnimation = ChaseAnimation(fuselights.ceiling, [ORANGE, YELLOW, GREEN], numCycles=90, blockSize=len(fuselights.ceiling), moveDelay=2)
bgAnimation = TwinkleFadeAnimation(fuselights.background, [ORANGE, BLUE, RED, ORANGE, PURPLE, GREEN], numCycles=900)
compositeAnimation = CompositeAnimation(ceilingAnimation, [bgAnimation])

if __name__ == '__main__':
	controls.startLightQueue()
	while True:
		flashAnimation.run()
	controls.stopLightQueue()
