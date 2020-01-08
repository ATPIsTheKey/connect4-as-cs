# Rules of Connect4:

- The first player starts Connect Four by dropping one of their yellow discs into the center column of an empty game board. The two players then alternate turns dropping one of their discs at a time into an unfilled column, until the second player, with red discs, achieves a diagonal four in a row, and wins the game. For games where the board fills up before either player achieves four in a row, then the games are a draw

# Game structure:

![flowchart](res/flowchart_guide.png)

# Module prototypes/ global variables:

| **Variable name** | **Type** | **Description** |
| --- | --- | --- |
| **Game\_board** | ARRAY[7][6] | tbd. |
| **Moves\_so\_far** | INTEGER | tbd. |

| **Module/ function name** | **parameters** | **return values** | **description** |
| --- | --- | --- | --- |
| **init\_game\_board()** | **game\_board:** ARRAY[7][6] as GLOBAL (by reference) | VOID | tbd. |
| **draw\_game\_board()** | **game\_board:** ARRAY[7][6] as LOCAL (by value) | VOID | tbd. |
| **input\_player\_move()** | VOID | **valid\_player\_move:** INTEGER | tbd. |
| **update\_board\_from\_player\_move()** | **game\_board:** ARRAY[7][6] as GLOBAL (by reference) <br/><br/>  **player\_move:** INTEGER as LOCAL (by value) | VOID | tbd. |
| **check\_gameboard\_win()** | **game\_board:** ARRAY[7][6] as LOCAL (by value) | **game\_won:** BOOLEAN | tbd. |
| **check\_game\_board\_full()** | **game\_board:** ARRAY[7][6] as LOCAL (by value) | **game\_board\_full:** BOOLEAN | tbd. |
| **output\_game\_winner()** | **winning\_player:** INTEGER as LOCAL (by value) | VOID | tbd. |
