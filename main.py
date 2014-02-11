#	 O | X | X
#	---+---+---
#	 O | O |  	TIC-TAC-TOE
#	---+---+---
#	 X | O | X

from functions import *
from botLogic import botMakesMove
from random import randrange
from Tkinter import Tk, Canvas, TOP

gameField = initMatrix(3,3,' ')
gameOver = False
redrawField(gameField)

print('<X> always start first, but it may be the bot or the player at random. To make a move - just click on the corresponding square in the GUI. The console in the GUI version is output-only. Enjoy!')
side = 'X'	#'X' moves first always, like the white in Chess
botMark = 'X' if randrange(0,2)==0 else 'O'
playerMark = 'X' if botMark == 'O' else 'O'
gameResult = 0
moveCount = 0

root = Tk()
root.title('TIC-TAC-TOE')
root.resizable(False,False)
can = Canvas(root,background="white",width=150,height=120)
can.pack(side = TOP)
for i in xrange(3):
	st=[]
	for j in xrange(3):
		y=i*30
		x=j*30
		st+=[can.create_polygon(x,y,x+30,y,x+30,y+30,x,y+30,fill='lightgray',outline='black')]

if botMark == 'X':
	botX, botY = botMakesMove(gameField, botMark)
	redrawField(gameField)
	if botMark == 'X':
		can.create_line(botY*30+5,botX*30+5,botY*30+25,botX*30+25)
		can.create_line(botY*30+5,botX*30+25,botY*30+25,botX*30+5)
	else:
		can.create_oval(botY*30+5,botX*30+5,botY*30+25,botX*30+25)
def callback(event):
	result = evaluateField(gameField)
	if result != 0:
		print(result)
		gameOver = True
		return
	inputCorrect = False
	while not inputCorrect:
		clickedY, clickedX = event.x/30, event.y/30 #this is reversed...
		if(gameField[clickedX][clickedY]==' '):
			gameField[clickedX][clickedY] = playerMark
			inputCorrect = True
			print('Player makes a move:')
			redrawField(gameField)
			if playerMark == 'X':
				can.create_line(clickedY*30+5,clickedX*30+5,clickedY*30+25,clickedX*30+25)
				can.create_line(clickedY*30+5,clickedX*30+25,clickedY*30+25,clickedX*30+5)
			else:
				can.create_oval(clickedY*30+5,clickedX*30+5,clickedY*30+25,clickedX*30+25)
			result = evaluateField(gameField)
			if result != 0:
				print(result)
				gameOver = True
				return
			side = botMark
	print('Bot makes a move:')
	botX, botY = 0,0 
	botY, botX = botMakesMove(gameField, botMark)
	redrawField(gameField)
	if botMark == 'X':
		can.create_line(botY*30+5,botX*30+5,botY*30+25,botX*30+25)
		can.create_line(botY*30+5,botX*30+25,botY*30+25,botX*30+5)
	else:
		can.create_oval(botY*30+5,botX*30+5,botY*30+25,botX*30+25)
	result = evaluateField(gameField)
	if result != 0:
		print(result)
		gameOver = True
		return
	side = playerMark
	#print('moveResult = '+str(moveResult))
can.bind("<Button-1>", callback)
root.mainloop()