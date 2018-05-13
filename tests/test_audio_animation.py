'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Audio Animation Test: Test animations synced with realtime audio on lights
'''

import logging
logging.basicConfig(level=logging.DEBUG)
from config import *

# -------------------- Lights --------------------

# import fuselights
# lights = fuselights.mainroom
l1			= Light(controls, 3, "TV", 0.5, 0.7)
l2			= Light(controls, 5, "TV", 0.5, 0.7)
lights = [l1, l2]

LOW_TS = 30
HIGH_BRI = 255
LOW_BRI = 120

step1H	= FadeToColorAnimation(lights, [BLUE], brightness=HIGH_BRI, tsTime=1, sTime=0)
step2H	= FadeToColorAnimation(lights, [PURPLE], brightness=HIGH_BRI, tsTime=1, sTime=0)
step3H	= FadeToColorAnimation(lights, [ORANGE], brightness=HIGH_BRI, tsTime=1, sTime=0)
step4H	= FadeToColorAnimation(lights, [PINK], brightness=HIGH_BRI, tsTime=1, sTime=0)
step1L	= FadeToColorAnimation(lights, [YELLOW], brightness=LOW_BRI, tsTime=LOW_TS, sTime=0)
step2L	= FadeToColorAnimation(lights, [RED], brightness=LOW_BRI, tsTime=LOW_TS, sTime=0)
step3L	= FadeToColorAnimation(lights, [GREEN], brightness=LOW_BRI, tsTime=LOW_TS, sTime=0)
step4L	= FadeToColorAnimation(lights, [BROWN], brightness=LOW_BRI, tsTime=LOW_TS, sTime=0)

animations = [
	(step1L, step1H),
	(step2L, step2H),
	(step3L, step3H),
	(step4L, step4H)
]

# -------------------- Audio --------------------

LOW_FREQ = 1800
HIGH_FREQ = 3500

RUN_SECONDS = 3000

class AudioLights(object):
	def __init__(self):
		self._frames = []
		self._animationStep = 0

	def animateAudio(self):
		audiotk.get_audio_with_callback(RUN_SECONDS, self.checkData)
		return self._frames

	def checkData(self, data, frame_count=None, time_info=None, status=None):
		self._frames.append(data)

		sample_freq = audiotk.freq_from_data(data)
		#logging.info("The freq is %f Hz." % (sample_freq))

		if sample_freq > LOW_FREQ:
			self.advanceAnimation(sample_freq)

		return (data, audiotk.pyaudio.paContinue)

	def advanceAnimation(self, freq):
		anim_num = self._animationStep % len(animations)
		if freq > HIGH_FREQ:
			logging.info("Animation Advanced - High: %f" % freq)
			animations[anim_num][1].run()
		else:
			logging.info("Animation Advanced - Low: %f" % freq)
			animations[anim_num][0].run()
		self._animationStep += 1


########################### Main ###########################
if __name__ == '__main__':
	huecontrols.startLightQueue()
	audioLights = AudioLights()
	frames = audioLights.animateAudio()
	#audiotk.save_to_file("recording.wav", frames)
	huecontrols.stopLightQueue()
