import os

def fixSubfolder():

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
def fixTopLevel():
	os.system('mv 0.png 00.png')
	os.system('mv 1.png 01.png')
	os.system('mv 2.png 02.png')
	os.system('mv 3.png 03.png')
	os.system('mv 4.png 04.png')
	os.system('mv 5.png 05.png')
	os.system('mv 6.png 06.png')
	os.system('mv 7.png 07.png')
	os.system('mv 8.png 08.png')
	os.system('mv 9.png 09.png')
	
if __name__ == '__main__':
	fixSubfolder()