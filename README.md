# Word Puzzle Solver
Efficient word puzzle solver given any NxM size puzzle and a set of strings (words) to find.

Creates a hash table indexing every character in the puzzle for fast lookup.  Randomizes initial character selection and direction of lookup to avoid targeted worst-case scenarios.

Standard word puzzle rules apply - valid possible directions are up, down, left, right, and any straight diagonals.

Example input file:
```
5x5
H A S D F
G E Y B H
J K L Z X
C V B L N
G O O D O
HELLO
GOOD
BYE
```

Example output to stdout:
```
HELLO 0:0 4:4
GOOD 4:0 4:3
BYE 1:3 1:1
```
