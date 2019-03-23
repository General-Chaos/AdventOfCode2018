import os
import mod5

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    compound = (f.readlines())[0]

answer1 = len(mod5.pair_destroy(compound))
print(f"The answer to day 5 part 1 is: {answer1}")

answer2 = mod5.shortest_remove_type(compound)
print(f'The answer to day 5 part 2 is: {answer2[1]} , the winning type was: {answer2[0]}')
