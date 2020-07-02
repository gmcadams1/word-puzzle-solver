# Word Puzzle Solver
Efficient word puzzle solver given any NxM size puzzle and a set of strings (words) to find.

Creates a hash table indexing every character in the puzzle for fast lookup.  Randomizes initial character selection and direction of lookup to avoid targeted worst-case scenarios.

Example input file:
```
3x3
A B C
D E F
G H I
ABC
AEI
```
Example output to stdout:
```
HELLO 0:0 4:4
GOOD 4:0 4:3
BYE 1:3 1:1
```
