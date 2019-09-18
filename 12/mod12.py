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
        octal_list = []
        for j in range(len(octal)):
            if octal[j] == '#':
                octal_list.append(True)
            else:
                octal_list.append(False)
        notes_octal.update({tuple(octal_list): result})
    return notes_octal


def fill_notes(notes):
    for i in product([True, False], repeat=5):
        octal_list = []
        for j in range(5):
            if i[j]:
                octal_list.append(True)
            else:
                octal_list.append(False)
        if tuple(octal_list) not in notes.keys():
            notes[tuple(octal_list)] = False
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

    @staticmethod
    def _get_new_plants(plants, rules):
        new_plants = set()
        start = min(plants)
        end = max(plants)
        octal_list = None
        for i in range(start - 2, end + 2):
            if octal_list == None:
                octal_list = []
                for j in range(5):
                    if (i - 2 + j) in plants:
                        octal_list.append(True)
                    else:
                        octal_list.append(False)
                if rules[tuple(octal_list)]:
                    new_plants.add(i)
                else:
                    pass
            else:
                octal_list = octal_list[1:]
                if (i + 2) in plants:
                    octal_list.append(True)
                else:
                    octal_list.append(False)
                if rules[tuple(octal_list)]:
                    new_plants.add(i)
        return new_plants

    def iterate(self, rules, rounds):
        for _ in range(rounds):
            self.plants = self._get_new_plants(self.plants, rules)

    @property
    def true_sum(self):
        return sum(self.plants)

    # For part 2 we wait for the linear regression to settle into a fixed line, then calculate
    def estimate_true_sum(self, rules, rounds):
        plants = self.plants.copy()
        rounds_reg_same = 0
        reg = (0, 0)
        round_c = 1
        while rounds_reg_same < 100:
            plants = self._get_new_plants(plants, rules)
            plants_reg = divmod(sum(plants), round_c)
            if plants_reg == reg:
                rounds_reg_same += 1
            else:
                reg = plants_reg
            round_c += 1
        return (rounds * reg[0]) + reg[1]


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
