import pyautogui
from PIL import Image,ImageGrab #pip install pillow
import time
# from numpy import asarray 

def hit(key):
	pyautogui.keyDown(key)

def isCollide(data):
	#for birds
	for i in range(480,530):
		for j in range(110,195):
			if data[i,j] < 100:
				hit("down")
				return True

	#for cactus
	for i in range(480,530):
		for j in range(197,245):
			if data[i,j] < 100:
				hit("up")
				return True
	return False



# def takeScreenshot():
# 	image=ImageGrab.grab().convert('L')
	
# 	return image

if __name__ == '__main__':
	print("Hey DinoGame is start in 3 sec")
	time.sleep(2)
	# hit("up")

	while True:
		image = ImageGrab.grab().convert('L')
		data = image.load()
		isCollide(data)
		
		# print(asarray(image))

	#draw the rectangle for cactus
'''		for i in range(480,530):
			for j in range(197,245):
				data[i,j] = 0

	#draw the rectangle for bird
		for i in range(480,530):
			for j in range(110,195):
				data[i,j] = 71

		image.show()
		break
'''





