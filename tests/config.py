'''
	@Harris Christiansen (code@harrischristiansen.com)
	Light Controls - https://github.com/harrischristiansen/lightcontrol_py
	Light Controller Config/Import File
'''

from HueControls import HueControls
from LightControl import *

# HUE_BRIDGE_IP = '10.3.0.177' # Fuse
# HUE_BRIDGE_API_KEY = 'd5orxbetHKF46FCV1wBmnFTVNSkGQWMSjwNOHu2i'
#HUE_BRIDGE_IP = '10.0.0.147' # 344
#HUE_BRIDGE_API_KEY = 'KJbQWzkdkUlhE8276UsldU3Ss7emfXBC4AxuzcBo'
HUE_BRIDGE_IP = '192.168.1.125' # Namans
HUE_BRIDGE_API_KEY = 'QeU9qwKYDc5Z1OqzhPMbrutdRwSKj9wDFgLUAii4'

controls = HueControls(HUE_BRIDGE_IP, HUE_BRIDGE_API_KEY)

WHITE	= controls.hexToXY("#FFFFFF")
RED		= controls.hexToXY("#FF0000")
GREEN	= controls.hexToXY("#00FF00")
BLUE	= controls.hexToXY("#0000FF")
ORANGE	= controls.hexToXY("#904000")
PINK	= controls.hexToXY("#800080")
YELLOW	= controls.hexToXY("#ffb400")
PURPLE	= controls.hexToXY("#bb00ff")
CYAN	= controls.hexToXY("#FFFFFF")
BROWN	= controls.hexToXY("#FFFFFF")