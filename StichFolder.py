import os

def main():

	for x in range(64):
		os.system('convert ' + str(x) + '/*.png -append ' + str(x) + '.png')

if __name__ == '__main__':
	main()