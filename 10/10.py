import os
import mod10

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    input_strings = [x.rstrip('\n') for x in f.readlines()]

lights = mod10.parse_input(input_strings)
min_lights = mod10.find_y_minima(lights)

problemoutput = os.path.join(fileDir, 'output.txt')
mod10.output_file(min_lights[0], problemoutput)
print(f"The answer to day 10 part 1 is in the file {problemoutput}")

answer2 = min_lights[1]
print(f"The answer to day 10 part 2 is: {answer2}")
