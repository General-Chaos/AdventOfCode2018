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
    result = set()
    for i in range(len(input_string)):
        if input_string[i] == '#':
            result.add(i)
        else:
            pass
    return result


class Plants():

    def __init__(self, plants):
        self.plants = plants

    def iterate(self, rules, rounds):
        for _ in range(rounds):
            new_plants = set()
            octals = [1, 2, 4, 8, 16]
            start = min(self.plants)
            end = max(self.plants)
            for i in range(start - 2, end + 2):
                octal_sum = 0
                for j in range(5):
                    if (i - 2 + j) in self.plants:
                        octal_sum += octals[j]
                    else:
                        pass
                if rules[octal_sum]:
                    new_plants.add(i)
                else:
                    pass
            self.plants = new_plants

    @property
    def true_sum(self):
        return sum(self.plants)


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
