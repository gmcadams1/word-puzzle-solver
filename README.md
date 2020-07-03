# Word Puzzle Solver
Efficient word puzzle solver given any NxM size puzzle and a set of strings (words) to find.

## Logic Overview
Create a 2D array representing the entire puzzle, and then create a hash table indexing every character in the puzzle for fast lookup.

Given a word to find, get the index of the first character in the 2D array.  Pick one of the indices randomly if duplicate first characters exists in the puzzle.

Choose a random valid direction to look at.

Then, for the rest of the word, compare each next character to the next adjacent character in the puzzle for equality.

If we ever go out of bounds, or if character equality comparison fails, stop and pick another direction.

Repeat for each direction, then repeat for each first character in the puzzle, if applicable.

As soon as an exact match is found, return the solution.

Randomizes the first character selection in the puzzle and the direction of lookup to avoid targeted worst-case scenarios.

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

## Included Test Cases
Input1: 14x14 puzzle with Simpsons characters

Input2: 54x88 stress-test puzzle with Pokemon
