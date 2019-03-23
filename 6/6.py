import os
import mod6

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    input = [x.rstrip('\n') for x in f.readlines()]

answer1 = mod6.get_largest_area(input)
print(f"The answer to day 6 part 1 is: {answer1}")

answer2 = mod6.get_area_under_dist(input, 10000)
print(f"The answer to day 6 part 2 is: {answer2}")
