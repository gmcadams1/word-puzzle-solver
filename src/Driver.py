"""
    File name: Driver.py
    Author: Gregory McAdams
    Date created: 6/30/2020
    Date last modified: 7/02/2020
    Python Version: 3.8
"""
from src.WordPuzzle import WordPuzzle

class Driver:
    def __init__(self, input):
        self.input = input
    
    # Main
    def run(self):
        # Read input file
        contents = open(self.input, 'r').read().split('\n')
        # Get rows and cols
        (rows, cols) = [int(x) for x in contents.pop(0).split('x')]
        # Build raw puzzle
        raw_puzzle = ""
        for i in range(rows):
            raw_puzzle += contents.pop(0)
            if i < rows-1:
                raw_puzzle += '\n'
        # Create Puzzle
        puzzle = WordPuzzle(rows, cols, raw_puzzle)
        # For each word to find
        for word in contents:
            # Find the word and return the start/end positions
            # Ex. ((0,0),(2,2))
            answer = puzzle.find_word(word)
            # If we didn't find the word
            if answer == None:
                print(word + ' not found')
            # Else, we found it
            else:
                (start,end) = answer
                print(
                    word
                    + ' ' + str(start[0]) + ':' + str(start[1])
                    + ' ' + str(end[0]) + ':' + str(end[1])
                )

if __name__ == '__main__':
    main = Driver('Input1.txt')
    main.run()