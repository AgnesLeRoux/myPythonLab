from random import randint
def showInstructions():
	print('''Instructions:
	You are the captain of the Simon, a treasure-hunting ship. Your current
	mission
	is to use sonar devices to find three sunken treasure chests at the
	bottom of
	the ocean. But you only have cheap sonar that finds distance, not
	direction.
			  
	Enter the coordinates to drop a sonar device. The ocean map will be
	marked with
	how far away the nearest chest is, or an X if it is beyond the sonar
	device's
	range. For example, the C marks are where chests are. The sonar device
	shows a
	3 because the closest chest is 3 spaces away.
			  
                1         2         3
	  012345678901234567890123456789012
	0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
	1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
	2 '~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
	3 ````````~~~`````~~~`~`````~`~``~` 3
	4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4		 
	  012345678901234567890123456789012
                1         2         3
	(In the real game, the chests are not visible in the ocean.)
			  
	Press enter to continue...''')
	input()		  
	print('''When you drop a sonar device directly on a chest, you
	retrieve it and the other
	sonar devices update to show how far away the next nearest chest is. The
	chests are beyond the range of the sonar device on the left, so it shows
	an X.
			  
                1         2         3
	  012345678901234567890123456789012	  
	0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
	1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
	2 '~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
	3 ````````~~~`````~~~`~`````~`~``~` 3
	4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4		  
	  012345678901234567890123456789012
	            1         2         3
			  
	The treasure chests don't move around. Sonar devices can detect treasure
	chests up to a distance of 9 spaces. Try to collect all 3 chests before
	running out of sonar devices. Good luck!
			  
	Press enter to continue...''')
	input()
	
def drawSolution(sea):
	toPrint = ''
	for i in range(len(sea)):
		for j in range(len(sea[0])):
			if sea[i][j]==0:
				toPrint += '.'
			else:
				toPrint += 'C'
		toPrint += '\n'
	print(toPrint)
	return None

def findSymbol(sea, revealed, coord1, coord2):
	if not revealed[coord1][coord2]:
		if randint(0, 1)==0:
			return '`'
		else:
			return '~'
	else:
		if sea[coord1][coord2]== 1:
			return 'C'
		else:
			return '?'

def drawFogOfWar(sea, revealed):
	nbRows = len(sea)
	nbCols = len(sea[0])
	toPrint = ''
	toPrint += '     '+'         '
	for j in range(1, nbCols//10):
		toPrint += str(j)+'         '
	toPrint += '\n'
	toPrint += '    '
	for j in range(0,nbCols//10):
		toPrint += '0123456789'
	toPrint += '\n'
	for i in range(nbRows):
		if i//10 >0:
			toPrint += ' '+str(i)+' '
		else:
			toPrint += '  '+str(i)+' '
		for j in range(nbCols):
			if sea[i][j]==0:
				toPrint += findSymbol(sea, revealed, i, j)
			else:
				toPrint += findSymbol(sea, revealed, i, j)
		toPrint += '\n'
	toPrint += '    '
	for j in range(0,nbCols//10):
		toPrint += '0123456789'
	toPrint += '\n'
	toPrint += '     '+'         '
	for j in range(1, nbCols//10):
		toPrint += str(j)+'         '
	toPrint += '\n'
	
	toPrint += '\n'
	print(toPrint)
	return None

def playGame():
	print('S O N A R')

	print('Would you like to view the instructions? (yes/no)')
	if input().lower().startswith('y'):
		showInstructions()

	nbRows = 15
	nbCols = 60
	sea = [[0 for _ in range(nbCols)] for _ in range(nbRows)]
	revealed = [[False for _ in range(nbCols)] for _ in range(nbRows)]

	coordC1 = [randint(0,nbRows-1),randint(0,nbCols-1)]

	coordC2 = [randint(0,nbRows-1),randint(0,nbCols-1)]
	while coordC2[0]==coordC1[0] and coordC2[1]==coordC1[1]:
		coordC2 = [randint(0,nbRows-1),randint(0,nbCols-1)]

	coordC3 = [randint(0,nbRows-1),randint(0,nbCols-1)]
	while coordC3[0]==coordC1[0] and coordC3[1]==coordC1[1] or coordC3[0]==coordC2[0] and coordC3[1]==coordC2[1]:
		coordC3 = [randint(0,nbRows-1),randint(0,nbCols-1)]

	sea[coordC1[0]][coordC1[1]]=1
	sea[coordC2[0]][coordC2[1]]=1
	sea[coordC3[0]][coordC3[1]]=1	
	#drawSolution(sea)
	drawFogOfWar(sea, revealed)

playGame()
