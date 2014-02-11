from functions import *
def detectPossibility(mark,field):#this function detects if there is an immedeate threat that mark can line up 3 peices and form a row
	"""
	Detects if it is possible for the player who
	is playing as 'mark' to win the game immedeately, in this turn.
	Effectively - detects lines that have 2 squares filled with <mark>, and an empty square.  
	"""
	#detect horizontal possibilities
	for y in xrange(3):
		lineThreat = 0
		for x in xrange(3):
			if field[y][x]==mark:
				lineThreat+=1
		if lineThreat==2:
			for x in xrange(3):
				if field[y][x] == ' ':
					return x,y
	#detect vertical possibilities
	for x in xrange(3):
		lineThreat = 0
		for y in xrange(3):
			if field[y][x]==mark:
				lineThreat+=1
		if lineThreat==2:
			for y in xrange(3):
				if field[y][x] == ' ':
					return x,y
	#detect diagonal possibilities
	diag1Threat = 0
	diag2Threat = 0
	for i in xrange(3):
		if field[i][i]==mark:
			diag1Threat += 1
		if field[i][2-i]==mark:
			diag2Threat += 1
	if diag1Threat == 2:
		for i in xrange(3):
			if field[i][i]==' ':
				return i,i
	if diag2Threat == 2:
		for i in xrange(3):
			if field[i][2-i]==' ':
				return 2-i,i
	return -1,-1	#no possibilities detected

#def detectDoubleThreat(mark,field):
#	return

#TODO this should be in other module
def makeBestMove(ourMark, field):
	"""
	If it's impossible to win the game immedeately, and there's no immedeate threat of the
	opponent winning - this function attempts to place the mark in a spot which seems to
	show the most chances to form a line of 3 marks some time later
	"""
	#if center free - go for it!
	if field[1][1]==' ':
		field[1][1]=ourMark
		return 1,1
	opponentMark = 'O' if ourMark=='X' else 'X'
	horizontal = [0,0,0]
	vertical = [0,0,0]
	diagonal1 = 0
	diagonal2 = 0
	#evaluate horizontals
	for y in xrange(3):
		for x in xrange(3):
			if field[y][x]==opponentMark:
				horizontal[y] -= 10
				break
			if field[y][x]==ourMark:
				horizontal[y] += 1
	#evaluate verticals
	for x in xrange(3):
		for y in xrange(3):
			if field[y][x]==opponentMark:
				vertical[x] -= 10
				break
			if field[y][x]==ourMark:
				vertical[x] += 1
	#evaluate diagonal1
	for i in xrange(3):
		if field[i][i]==opponentMark:
			diagonal1 -= 10
			break
		if field[i][i]==ourMark:
			diagonal1 += 1
	#evaluate diagonal2
	for i in xrange(3):
		if field[i][2-i]==opponentMark:
			diagonal2 -= 10
			break
		if field[i][2-i]==ourMark:
			diagonal2 += 1
	#now we evaluate the expected utility of putting a mark in each of the occupied squares
	p = initMatrix(3,3,0)
	p[0][0] = horizontal[0]+vertical[0]+diagonal1
	p[0][1] = horizontal[0]+vertical[1]
	p[0][2] = horizontal[0]+vertical[2]+diagonal2
	p[1][0] = horizontal[1]+vertical[0]
	p[1][1] = horizontal[1]+vertical[1]+diagonal1+diagonal2
	p[1][2] = horizontal[1]+vertical[2]
	p[2][0] = horizontal[2]+vertical[0]+diagonal2
	p[2][1] = horizontal[2]+vertical[1]
	p[2][2] = horizontal[2]+vertical[2]+diagonal1
	#now we just find and put ourMark into the square with maximum expected utility
	maxp,xmax,ymax = -1000,0,0
	for y in xrange(3):
		for x in xrange(3):
			if (field[y][x]==' ' and p[y][x] <= -18):
				field[y][x] = ourMark
				return x, y
			if (field[y][x]==' ' and p[y][x] > maxp):
				maxp = p[y][x]
				xmax,ymax = x,y
	field[ymax][xmax] = ourMark
	return xmax, ymax
def botMakesMove(field, botMark):#botMark is either 'X' or 'O', field is the current state of the game field
	"""	The high-level logic of the AI """
	if botMark=='X':
		opponentMark='O'
	else:
		opponentMark='X'
	#detect if it's possible to win the game immedeately:
	possibilityX,possibilityY = detectPossibility(botMark, field)
	if possibilityX >= 0:
		field[possibilityY][possibilityX] = botMark
		return possibilityX,possibilityY	#the bot has won!
	#if we can't win right now - we must detect and block any immedeate threats of the opponentMark winning:
	threatX,threatY = detectPossibility(opponentMark, field)
	if threatX >= 0:		#if any threat detected - block immedeately
		field[threatY][threatX] = botMark
		return threatX, threatY
	#general case
	return makeBestMove(botMark, field)