'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Controls: Basic test lighting controls
'''

HUE_BRIDGE_IP = '10.3.0.177'
HUE_BRIDGE_API_KEY = 'd5orxbetHKF46FCV1wBmnFTVNSkGQWMSjwNOHu2i'

from HueControls import HueControls

controls = HueControls(HUE_BRIDGE_IP, HUE_BRIDGE_API_KEY)
color = controls.hexToXY("#FF0000")
controls.setLight(17, color)
#controls.setLightHue(17, 30000)