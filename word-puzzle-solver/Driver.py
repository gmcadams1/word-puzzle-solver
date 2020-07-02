from WordPuzzle import WordPuzzle

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
        self.puzzle = WordPuzzle(rows, cols, raw_puzzle)
        # For each word to find
        for word in contents:
            # Find the word
            answer = self.puzzle.find_word(word)
            # Blank end position - didn't find it
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