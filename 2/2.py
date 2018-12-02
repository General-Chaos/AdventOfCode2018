import os
import mod2

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    problemdata = [mod2.Box(line.rstrip('\n')) for line in f.readlines()]

answer1 = mod2.get_boxlist_checksum(problemdata)
print(f"The answer to day 2 part 1 is: {answer1}")

match = mod2.get_first_matching_boxes(problemdata)
answer2 = match[0].get_shared_letters(match[1])
print(f"The answer to day 2 part 2 is: {answer2}")
