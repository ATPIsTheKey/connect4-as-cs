# Rules of Connect4

- The first player starts Connect Four by dropping one of their yellow discs
 into the center column of an empty game board. The two players then alternate turns dropping one of their discs at a time into an unfilled column, until the second player, with red discs, achieves a diagonal four in a row, and wins the game. For games where the board fills up before either player achieves four in a row, then the games are a draw.

# Game structure

![flowchart](res/flowchart_guide.png)

# Module prototypes/global variables

| **Variable name** | **Type** | **Description** |
| --- | --- | --- |
| **Game\_board** | `ARRAY[7][6]` | ...|
| **Moves\_so\_far** | `INTEGER` | ...|

| **Module/function name** | **Parameters** | **Return values** | **Description** |
| --- | --- | --- | --- |
| **init\_game\_board()** | **game\_board:** `ARRAY[7][6]` as `GLOBAL (by reference)` | `VOID` | ...|
| **draw\_game\_board()** | **game\_board:** `ARRAY[7][6]` as `LOCAL (by value)` | `VOID` | ...|
| **input\_player\_move()** | `VOID` | **valid\_player\_move:** `INTEGER` | ...|
| **update\_board\_from\_player\_move()** | **game\_board:** `ARRAY[7][6]` as `GLOBAL (by reference)` <br/><br/>  **player\_move:** `INTEGER` as `LOCAL (by value)` | `VOID` | ...|
| **check\_gameboard\_win()** | **game\_board:** `ARRAY[7][6]` as `LOCAL (by value)` | **game\_won:** `BOOLEAN` | ...|
| **check\_game\_board\_full()** | **game\_board:** `ARRAY[7][6]` as `LOCAL (by value)` | **game\_board\_full:** `BOOLEAN` | ...|
| **output\_game\_winner()** | **winning\_player:** `INTEGER` as `LOCAL (by value)` | `VOID` | ...|

# Setting up your python environment
- To make sure all libraries can be imported, run`pip install -r requirements
.txt --no-index --find-links file:///tmp/packages` in this project's directory
  before running the program.
 - Also, you have to use Python 3.

# A quick introduction to git
## Basic commands
- $ `git init : initialise new repository.`
- $ `git status : prints status information.`
- $ `git add <file> : stage a file.`
- $ `git rm <file> : remove file and stage the removal.`
- $ `git reset HEAD <file> : unstage file.`
- $ `git checkout [–] <file> : revert file to last committed
version (snapshot).`
- $ `git diff : prints differences between working tree and
index (stage area).`
- $ `git log : show commit history.`
- $ `git commit : commit currently staged files (create new
snapshot).`
