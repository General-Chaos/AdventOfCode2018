import os
import mod4

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')

with open(probleminput) as f:
    problemdata = mod4.process_event_stream([mod4.parse_log_line(line.rstrip('\n')) for line in f.readlines()])

most_slept = mod4.get_most_slept(problemdata)
answer1 = most_slept['id'] * most_slept['most_slept_min']
print(f"The answer to day 4 part 1 is: {answer1}")

max_min_slept = mod4.get_max_min_slept(problemdata)
answer2 = max_min_slept['id'] * max_min_slept['most_slept_min']
print(f"The answer to day 4 part 2 is: {answer2}")
