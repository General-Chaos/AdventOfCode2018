import os
import mod1

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    problemdata = [int(line.rstrip('\n')) for line in f.readlines()]

answer1 = None
for answer1 in mod1.get_offsets(0, problemdata):
    pass

print(f"The answer to day 1 part 1 is: {answer1}")

answer2 = mod1.get_first_repeat(0, problemdata)

print(f"The answer to day 1 part 2 is: {answer2}")
