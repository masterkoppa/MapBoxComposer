import os

def main():

	for x in range(64):
		os.system('mv ' + str(x) + '/0.png ' + str(x) + '/00.png')
		os.system('mv ' + str(x) + '/1.png ' + str(x) + '/01.png')
		os.system('mv ' + str(x) + '/2.png ' + str(x) + '/02.png')
		os.system('mv ' + str(x) + '/3.png ' + str(x) + '/03.png')
		os.system('mv ' + str(x) + '/4.png ' + str(x) + '/04.png')
		os.system('mv ' + str(x) + '/5.png ' + str(x) + '/05.png')
		os.system('mv ' + str(x) + '/6.png ' + str(x) + '/06.png')
		os.system('mv ' + str(x) + '/7.png ' + str(x) + '/07.png')
		os.system('mv ' + str(x) + '/8.png ' + str(x) + '/08.png')
		os.system('mv ' + str(x) + '/9.png ' + str(x) + '/09.png')
if __name__ == '__main__':
	main()