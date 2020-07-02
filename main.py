from src.WordPuzzle import *
from src.Driver import *

if __name__ == '__main__':
    print("---TEST 1---")
    main = Driver('input_files/Input1.txt')
    main.run()
    print("---TEST 2---")
    main = Driver('input_files/Input2.txt')
    main.run()