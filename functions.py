def initMatrix(height, width, initValue):
	"""Initialized a matrix of given size with given values"""
	field = []
	for y in xrange(height):
		field.append([])
		for x in xrange(width):
			field[y].append(initValue)
	return field
def redrawField(field):
	"""Dumps the current game field state as psaudographics to the console"""
	print(' '+field[0][0]+' | '+field[0][1]+' | '+field[0][2])
	print('---+---+---')
	print(' '+field[1][0]+' | '+field[1][1]+' | '+field[1][2])
	print('---+---+---')
	print(' '+field[2][0]+' | '+field[2][1]+' | '+field[2][2])
	return
def evaluateField(field):
	"""Checks if the game is in a win or lose condition"""
	emptyCount = 9
	for y in xrange(3):
		lineX,lineO = 0,0
		for x in xrange(3):
			if field[y][x]=='X':
				lineX += 1
				emptyCount -= 1
			if field[y][x]=='O':
				lineO += 1
				emptyCount -= 1
		if lineX == 3:
			return 'X has won!'
		if lineO == 3:
			return 'O has won!'
	if emptyCount == 0:
		return 'Tie!'
	for x in xrange(3):
		lineX,lineO = 0,0
		for y in xrange(3):
			if field[y][x]=='X':
				lineX += 1
			if field[y][x]=='O':
				lineO += 1
		if lineX == 3:
			return 'X has won!'
		if lineO == 3:
			return 'O has won!'
	diag1X, diag1O,diag2X,diag2O = 0,0,0,0
	for i in xrange(3):
		if field[i][i] == 'X':
			diag1X += 1
		if field[i][i] == 'O':
			diag1O += 1
		if field[i][2-i] == 'X':
			diag2X += 1
		if field[i][2-i] == 'O':
			diag2O += 1
	if diag1X == 3 or diag2X == 3:
		return 'X has won!'
	if diag1O == 3 or diag2O == 3:
		return 'O has won!'
	return 0 