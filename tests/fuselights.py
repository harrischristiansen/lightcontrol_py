'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Fuse Lights: Light definitions for Fuse
'''

from config import *

window		= Light(controls, 5, "Window", 0.5, 0.9)
couch		= Light(controls, 6, "Couch", 0.5, 0.8)
mid			= Light(controls, 8, "Middle", 0.5, 0.6)
tv			= Light(controls, 9, "TV", 0.5, 0.7)
wall		= Light(controls, 7, "Wall", 0.1, 0.9)
tvstand		= Light(controls, 18, "TV Stand", 0.1, 0.75)
fridge		= Light(controls, 4, "Fridge", 0.85, 0.25)
sink		= Light(controls, 19, "Sink", 0.6, 0.1)
oven		= Light(controls, 20, "Oven", 0.6, 0.2)
bar			= Light(controls, 21, "Bar", 0.6, 0.3)
cabinet		= Light(controls, 26, "Cabinet", 0.9, 0.15)
table		= Light(controls, 27, "Table", 0.4, 0.77)
lamp_mid	= Light(controls, 10, "Lamp Mid", 0.86, 0.86)
lamp_top	= Light(controls, 11, "Lamp Top", 0.91, 0.91)
lamp_btm	= Light(controls, 12, "Lamp Bottom", 0.81, 0.81)
bath_main	= Light(controls, 16, "Main Bathroom", 0.9, 0.5)
bath_guest	= Light(controls, 17, "Guest Bathroom", 0.1, 0.5)

kitchen = [sink, oven, bar, fridge, cabinet]
living = [window, couch, tv, mid, wall, tvstand, table]
guest = [lamp_top, lamp_mid, lamp_btm]
bath = [bath_main, bath_guest]

mainroom = kitchen+living
alllights = kitchen+living+guest+bath