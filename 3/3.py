import os
import mod3

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    problemdata = [line.rstrip('\n') for line in f.readlines()]

fabric = mod3.Fabric(1000, 1000)

for i in problemdata:
    fabric.add_claim(i)

answer1 = fabric.get_overclaimed_area()
print(f"The answer to day 3 part 1 is: {answer1}")

answer2 = fabric.get_first_nooverlap()
print(f"The answer to day 3 part 2 is: {answer2}")
