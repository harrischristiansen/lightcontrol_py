'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	CompositeAnimation: Animation composed of multiple animations running concurrently
'''

import threading

class CompositeAnimation(object):
	def __init__(self, primaryAnimation, otherAnimations=[]):
		# if (not isinstance(lights, list)) or (not isinstance(lights[0], Light)):
		# 	raise ValueError("lights must be a list of Light Objects")

		self._primaryAnim = primaryAnimation			# Primary Animation to run (controls length)
		self._otherAnims = otherAnimations				# List of additional animations to run

	def run(self):
		for animation in self._otherAnims: # Start background animations
			self._spawn(self.startBGAnimation, animation)

		self._primaryAnim.run() # Run primary animation

		for animation in self._otherAnims: # Stop all background animations
			animation.stop()


	def startBGAnimation(self, animation):
		animation.run()

	def _spawn(self, f, *args):
		t = threading.Thread(target=f, args=args)
		t.daemon = True
		t.start()