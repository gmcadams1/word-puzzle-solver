import sys
from src.WordPuzzle import *
from src.Driver import *

if __name__ == '__main__':
    # Run custom test(s)
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print("---" + arg + "---")
            main = Driver(arg)
            main.run()

    # Run default tests
    else:
        print("---TEST 1---")
        main = Driver('input_files/Input1.txt')
        main.run()
        print("---TEST 2---")
        main = Driver('input_files/Input2.txt')
        main.run()
        print("Completed Tests")