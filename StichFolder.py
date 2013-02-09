import os
import FixFilenames

def stichVertical():

	for x in range(64):
		os.system('convert ' + str(x) + '/*.png -append ' + str(x) + '.png')

def stichHorizontal():
	FixFilenames.fixTopLevel()
	os.system('convert *.png -append composite.png')

if __name__ == '__main__':
	stichVertical()
	stichHorizontal()