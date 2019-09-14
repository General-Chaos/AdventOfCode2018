import os
import mod12

fileDir = os.path.dirname(os.path.realpath(__file__))
probleminput = os.path.join(fileDir, 'input.txt')
notes_input = os.path.join(fileDir, 'notes.txt')

with open(probleminput) as f:
    plants = mod12.parse_input(f.read())

with open(notes_input) as f:
    notes = mod12.parse_notes([x.rstrip('\n') for x in f.readlines()])

plants = mod12.Plants(plants)
plants.iterate(notes, 20)

print(f"The answer to day 12 part 1 is: {plants.true_sum}")

plants.iterate(notes, 49999999980)
print(f"The answer to day 10 part 2 is: {plants.true_sum}")
