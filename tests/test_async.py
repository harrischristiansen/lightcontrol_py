import requests
import time
import json

from multiprocessing import Pool

data_red = json.dumps({"bri": 255, "transitiontime": 0, "xy": [0.675, 0.322]})
data_blue = json.dumps({"bri": 255, "transitiontime": 0, "xy": [0.167, 0.04]})

def setLight(lightID, color):
	requests.put("http://10.0.0.147/api/KJbQWzkdkUlhE8276UsldU3Ss7emfXBC4AxuzcBo/lights/"+str(lightID)+"/state", data=color)

def playAnimation(lightID):
	p = Pool(5)

	for i in range(10):
		#setLight(lightID, data_red)
		p.apply_async(setLight, (6, data_red))
		p.apply_async(setLight, (7, data_red))
		time.sleep(0.2)
		#setLight(lightID, data_blue)
		p.apply_async(setLight, (6, data_blue))
		p.apply_async(setLight, (7, data_blue))
		time.sleep(0.2)

lights = [6,7]
if __name__ == '__main__':
	playAnimation(6)
	#p = Pool(5)
	#print(p.map(playAnimation, lights))
