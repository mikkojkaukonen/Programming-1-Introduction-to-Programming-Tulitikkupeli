# Programming-1-Introduction-to-Programming-Tulitikkupeli
Tampere University, Projects made in the course Programming 1: Introduction to Programming

Assignment

In the olden days them kids didn't have no fancy mobile communication devices to play with. They have to come up with fun stuff to do using their imagination. One of these exciting pieces of entertainment was a game called 21 matchsticks, or something on those lines. The idea of the game was to lay 21 (match)sticks on the table between two players and then the players would take turns to pick 1–3 sticks from the pile. The player who was forced to take the last stick lost the game. Simple as that. Your job in this assignment is to create a modern computer version of this game.

Program's Behavior

When the program starts it prints on screen

Game of sticks

Player 1 enter how many sticks to remove:

and waits for the first player to input how many sticks she wants to draw. If the player doesn't enter an integer between 1–3, the program immediatelly prints an error message:

Must remove between 1-3 sticks!

and asks the layer to enter a number again.

Player 1 enter how many sticks to remove:

Once the player enters an acceptable number is sticks, the game tells the players how many sticks are left:

There are X sticks left

where X should be replaced with the number of sticks left. This printout does not happen when the game ends i.e. the game doesn't report the situation when there are no sticks left.

To be user friendly the game will always let the players know whose turn it is. Continuing the example above, when player 1 has successfully drawn some sticks from the pile, the program outputs:

Player 2 enter how many sticks to remove:

and waits the player 2 to pick up some sticks.

The player who draws the last stick loses the game. When this happens, the game prints:

Player Y lost the game!

where Y is the number (1 or 2) of the losing player.

If a player tries to draw more sticks than there are left in the pile, he also loses as happens in the example below.

Complete example run

Here is a complete example of one full game:

Game of sticks

Player 1 enter how many sticks to remove: 2

There are 19 sticks left

Player 2 enter how many sticks to remove: 4

Must remove between 1-3 sticks!

Player 2 enter how many sticks to remove: 0

Must remove between 1-3 sticks!

Player 2 enter how many sticks to remove: 2

There are 17 sticks left

Player 1 enter how many sticks to remove: 3

There are 14 sticks left

Player 2 enter how many sticks to remove: 1

There are 13 sticks left

Player 1 enter how many sticks to remove: 3

There are 10 sticks left

Player 2 enter how many sticks to remove: 2

There are 8 sticks left

Player 1 enter how many sticks to remove: 3

There are 5 sticks left

Player 2 enter how many sticks to remove: 1

There are 4 sticks left

Player 1 enter how many sticks to remove: 2

There are 2 sticks left

Player 2 enter how many sticks to remove: 1

There are 1 sticks left

Player 1 enter how many sticks to remove: 3

Player 1 lost the game!
