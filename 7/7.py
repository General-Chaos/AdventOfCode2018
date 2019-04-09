import os
import mod7

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    input_strings = [x.rstrip('\n') for x in f.readlines()]

answer1 = mod7.get_order(mod7.parse_input(input_strings))
print(f"The answer to day 7 part 1 is: {answer1}")
