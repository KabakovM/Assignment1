TIC-TAC-TOE by Kabakov Mikhail, Feb. 2014
Implemented in Python ver. 2.7.6 x64

The game consists of 3 files:
main.py - this files is used to start the game, contains the very high-level logic of the game
botLogic.py - the implementation of botMakesMove() method and its child methods - the algorithms the AI uses to calculate where to put its mark.
functions.py - a few rather routine methods that are necessary for the game to run but are not interesting from the point of view of AI or the high-level architecture.

the game is started by launching main.py with Python. It opens both a console and a small GUI window titled 'TIC-TAC-TOE'
The GUI is used to play the game by clicking on the squares with a mouse, while the console logs the game state after each move, and outputs additional information.

The starting mark is always the <X>, but whether it is the player or the AI who starts the game is determined by a random number.
If it is the AI - then you will see the game board having an <X> on it as soon as you start the game, and you respond with placing <O>s.
Otherwise it means that the game is waiting for the player to put the first <X> - and this is briefly explained in the console immedeately after game launch.