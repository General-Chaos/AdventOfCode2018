import os
import mod8

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    input_string = (f.readlines())[0]
    input_ints = [int(x) for x in input_string.split(" ")]

license_file = mod8.process_license(input_ints)[1][0]

answer1 = sum(mod8.yield_metadata(license_file))
print(f"The answer to day 8 part 1 is: {answer1}")

answer2 = mod8.get_root_node_value(license_file)
print(f"The answer to day 8 part 2 is: {answer2}")
