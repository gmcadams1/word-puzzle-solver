import random

class WordPuzzle:
    def __init__(self, rows, cols, raw_puzzle):
        self.rows = rows
        self.cols = cols
        self.raw_puzzle = raw_puzzle
        self.array_puzzle = []      # 2d char array to represent puzzle
        self.lookup = {}            # Index each char in puzzle
        self.create_puzzle()
    
    # Return int value for a char
    def hash_fn(self, char):
        return ord(char)
    
    # Init puzzle and data structures
    def create_puzzle(self):
        # Create char 2d array and hash table for fast lookup
        for line_idx, line in enumerate(self.raw_puzzle.split('\n')):
            row = []
            for letter_idx, letter in enumerate(line.split(' ')):
                row.append(letter)
                if self.hash_fn(letter) not in self.lookup:
                    self.lookup[self.hash_fn(letter)] = []
                self.lookup[self.hash_fn(letter)].append((line_idx,letter_idx))
            self.array_puzzle.append(row)
    
    # Try to find a word in the puzzle
    # Return ((start_row,start_col),(end_row,end_col))
    def find_word(self, word):
        full_pos = None
        
        # Get indexed location of first letter in the target word
        # Randomize order in which first letter location is picked
        random.shuffle(self.lookup[self.hash_fn(word[0])])
        for start_row,start_col in self.lookup[self.hash_fn(word[0])]:
            dirs = [
                'LEFT', 'RIGHT', 'UP', 'DOWN', 
                'UPLEFT', 'UPRIGHT', 'DOWNLEFT', 'DOWNRIGHT'
            ]
            # Randomize pick order of direction exploration
            random.shuffle(dirs)
            for dir in dirs:
                # Get the end coordinates as a tuple if word is found
                end_pos = self.__go_dir(start_row, start_col, word, dir)
                # If we received a non-empty tuple
                if len(end_pos) > 0:
                    full_pos = ((start_row,start_col),end_pos)
                    break
            if full_pos != None:
                break
                
        return full_pos
    
    # Return (end_row,end_col)
    def __go_dir(self, start_x, start_y, word, dir):
        match_count = 1
        end_pos = ()
        x = None
        y = None
                
        # All possible direction ranges in x and y for the word
        neg_x = range(start_x-1, start_x-1-len(word[1:]), -1)
        neg_y = range(start_y-1, start_y-1-len(word[1:]), -1)
        pos_x = range(start_x+1, start_x+1+len(word[1:]), 1)
        pos_y = range(start_y+1, start_y+1+len(word[1:]), 1)
        
        # Determine which ranges we use based on direction
        if 'LEFT' in dir:
            y = neg_y
        elif 'RIGHT' in dir:
            y = pos_y       
            
        if 'UP' in dir:
            x = neg_x        
        elif 'DOWN' in dir:
            x = pos_x
        
        # If we run into OOB exception, then the direction is not possible
        try:
            # Right or left
            if x == None:
                for rest_y in y:
                    if self.array_puzzle[start_x][rest_y] != word[match_count]:
                        break
                    else:
                        end_pos = (start_x,rest_y)
                        match_count += 1
            # Up or down
            elif y == None:
                for rest_x in x:
                    if self.array_puzzle[rest_x][start_y] != word[match_count]:
                        break
                    else:
                        end_pos = (rest_x,start_y)
                        match_count += 1
            # Diagonals
            else:
                for rest_x in x:
                    for rest_y in y:
                        # If equal distance from starting point (i.e. diagonal)
                        if abs(rest_x-start_x) == abs(rest_y-start_y):
                            if self.array_puzzle[rest_x][rest_y] != word[match_count]:
                                break
                            else:
                                end_pos = (rest_x,rest_y)
                                match_count += 1
            # If we didn't match the full word
            if match_count != len(word):
                end_pos = ()
        # Ran out of bounds - direction not possible given the word
        except IndexError:
            end_pos = ()
        
        # Returns ending position as tuple if entire word was matched
        return end_pos