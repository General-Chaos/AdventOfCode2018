import re
from itertools import product as product


def parse_notes(notes):
    notes_octal = dict()
    regex = r"(\S+) => (\S+)"
    for i in notes:
        match = re.match(regex, i)
        if match.group(2) == '#':
            result = True
        else:
            result = False
        octal = list(match.group(1))
        octal_sum = 0
        for j in range(len(octal)):
            if octal[j] == '#':
                octal_sum += pow(2, j)
        notes_octal.update({octal_sum: result})
    return notes_octal


def fill_notes(notes):
    for i in product([True, False], repeat=5):
        octal_sum = 0
        for j in range(5):
            if i[j]:
                octal_sum += pow(2, j)
            else:
                pass
        if octal_sum not in notes.keys():
            notes[octal_sum] = False
        else:
            pass
    return notes


def parse_input(input_string):
    result = []
    for i in range(len(input_string)):
        if input_string[i] == '#':
            result.append((i, True))
        else:
            result.append((i, False))
    return result


class Plants():

    def __init__(self, plants):
        self.plants = plants

    def iterate(self, rules, rounds):
        for _ in range(rounds):
            new_plants = list()
            start = self.plants[0][0]
            for i in range(-2, (len(self.plants)+2)):
                octal = list()
                octal_sum = 0
                for j in range((i - 2), (i + 3)):
                    if j < 0 or j >= (len(self.plants)):
                        octal.append(False)
                    else:
                        octal.append(self.plants[j][1])
                for j in range(len(octal)):
                    if octal[j]:
                        octal_sum += pow(2, j)
                    else:
                        pass
                new_plants.append((i + start, rules[octal_sum]))
            self.plants = new_plants

    @property
    def true_sum(self):
        return sum([x[0] for x in self.plants if x[1]])


if __name__ == "__main__":
    notes = [
        "...## => #",
        "..#.. => #",
        ".#... => #",
        ".#.#. => #",
        ".#.## => #",
        ".##.. => #",
        ".#### => #",
        "#.#.# => #",
        "#.### => #",
        "##.#. => #",
        "##.## => #",
        "###.. => #",
        "###.# => #",
        "####. => #",
        "..... => ."
    ]
    notes = parse_notes(notes)
    notes = fill_notes(notes)
    plant_string = "#..#.#..##......###...###"
    plants = Plants(parse_input(plant_string))
    plants.iterate(notes, 20)
    assert plants.true_sum == 325
