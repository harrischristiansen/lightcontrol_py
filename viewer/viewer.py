'''
	@Harris Christiansen (code@HarrisChristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Viewer: UI for Light Controls
'''

import logging
import pygame
import threading
import time

if __name__ == '__main__':
	from colors import *
else:
	from .colors import *

# UI Properies
FONT_SIZE = 16
FONT_LRG_SIZE = 22
LIGHT_WIDTH = 20
TITLE_ROW_HEIGHT = 35
ACTIONBAR_ROW_HEIGHT = 25
ACTIONBAR_BTN_WIDTH = 80
LIGHT_ROW_HEIGHT = 300
ROWS = [TITLE_ROW_HEIGHT, ACTIONBAR_ROW_HEIGHT, LIGHT_ROW_HEIGHT]
WINDOW_WIDTH = ACTIONBAR_BTN_WIDTH*3

class ControlsViewer(object):
	def __init__(self, windowTitle=None):
		self._runPygame = True
		self._windowTitle = windowTitle
		self._receivedUpdate = False
		self._showLights = False
		self._actions = [None, None]

	def mainViewerLoop(self):
		while not self._receivedUpdate: # Wait for first update
			time.sleep(0.5)

		self._initViewier()

		while self._runPygame:
			for event in pygame.event.get(): # User did something
				if event.type == pygame.QUIT: # User clicked quit
					self._runPygame = False # Flag done
				elif event.type == pygame.MOUSEBUTTONDOWN: # Mouse Click
					self._handleClick(pygame.mouse.get_pos())
				elif event.type == pygame.KEYDOWN: # Key Press Down
					self._handleKeypress(event.key)

			if self._receivedUpdate:
				self._drawViewer()
				self._receivedUpdate = False

			time.sleep(0.2)

		pygame.quit() # Done. Quit pygame.

	''' ======================== Public calls to set viewer attributes/callbacks ======================== '''

	def setTitle(self, title):
		self._title = title
		self._receivedUpdate = True
		return self

	def setLights(self, lights):
		self._lights = lights
		self._showLights = True
		self._receivedUpdate = True
		return self

	def setAction(self, index, action):
		self._actions[index] = action

	''' ======================== PRIVATE METHODS - Viewer Init - PRIVATE METHODS ======================== '''

	def _initViewier(self):
		pygame.init()

		# Set Window Size
		window_height = sum(ROWS)
		window_width = WINDOW_WIDTH
		self._window_size = (window_width, window_height)
		self._screen = pygame.display.set_mode(self._window_size)

		# Set Window Title
		window_title = "Lighting Controls"
		if self._windowTitle != None:
			window_title = self._windowTitle
		pygame.display.set_caption(window_title)

		# Create fonts
		self._font = pygame.font.SysFont('Arial', FONT_SIZE)
		self._fontLrg = pygame.font.SysFont('Arial', FONT_LRG_SIZE)

		# Create Pygame Clock
		self._clock = pygame.time.Clock()

	''' ======================== Handle Clicks ======================== '''

	def _handleClick(self, pos): # pos = [x, y], top:y=0
		logging.debug("Click %s" % str(pos))
		if pos[1] > TITLE_ROW_HEIGHT and pos[1] < TITLE_ROW_HEIGHT+ACTIONBAR_ROW_HEIGHT:
			self._handleActionClick(pos[0])

	def _handleActionClick(self, x):
		if x < ACTIONBAR_BTN_WIDTH: # Action 1
			logging.debug("Action 1 clicked")
			if self._actions[0] != None:
				self._actions[0]()
		elif x < ACTIONBAR_BTN_WIDTH*2: # Action 2
			logging.debug("Action 2 clicked")
			if self._actions[1] != None:
				self._actions[1]()
		self._receivedUpdate = True # Request Redraw

	''' ======================== Handle Keypresses ======================== '''

	def _handleKeypress(self, key):
		if key == pygame.K_LEFT:
			logging.debug("Left Key Pressed")
		elif key == pygame.K_RIGHT:
			logging.debug("Right Key Pressed")
		elif key == pygame.K_UP:
			logging.debug("Up Key Pressed")
		elif key == pygame.K_DOWN:
			logging.debug("Down Key Pressed")

	''' ======================== Viewer Drawing ======================== '''

	def _drawViewer(self):
		self._screen.fill(BLACK) # Set BG Color
		self._drawTitle()
		self._drawActionbar()
		if self._showLights:
			self._drawLights()

		self._clock.tick(60) # Limit to 60 FPS
		pygame.display.flip() # Update screen with new drawing

	def _drawTitle(self):
		pos_top = 0

		self._screen.blit(self._fontLrg.render(self._title, True, WHITE), (10, pos_top+4))

	def _drawActionbar(self):
		pos_top = TITLE_ROW_HEIGHT

		# Action 1 Button
		pygame.draw.rect(self._screen, BLUE, [0, pos_top, ACTIONBAR_BTN_WIDTH, ACTIONBAR_ROW_HEIGHT])
		self._screen.blit(self._font.render("Action 1", True, WHITE), (10, pos_top+4))

		# Toggle Exit on Game Over Button
		pygame.draw.rect(self._screen, GREEN_DARK, [ACTIONBAR_BTN_WIDTH, pos_top, ACTIONBAR_BTN_WIDTH, ACTIONBAR_ROW_HEIGHT])
		self._screen.blit(self._font.render("Action 2", True, WHITE), (ACTIONBAR_BTN_WIDTH+10, pos_top+4))

	def _drawLights(self):
		pos_top = sum(ROWS[0:2])
		height = LIGHT_ROW_HEIGHT
		width = WINDOW_WIDTH

		for light in self._lights:
			radius = int(LIGHT_WIDTH/2)
			top = pos_top + int(height * light.y) + radius
			left = int(width * light.x) + radius
			pygame.draw.circle(self._screen, BLUE, [left, top], radius)

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	filename = __file__[__file__.rfind('/')+1:]
	logging.debug("%s called on it's own, performing self test" % filename)
	viewer = ControlsViewer("Window Title")
	viewer.setTitle("Item Title")
	viewer.mainViewerLoop()
