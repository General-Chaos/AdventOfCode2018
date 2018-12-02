from itertools import groupby, combinations


class Box():

    def __init__(self, code: str):
        self.code = code
        self.hasdouble = 2 in [len(list(x[1])) for x in groupby(sorted(code))]
        self.hastriple = 3 in [len(list(x[1])) for x in groupby(sorted(code))]

    def __eq__(self, other):
        diffs = 0
        for i in range(len(self.code)):
            if self.code[i] == other.code[i]:
                pass
            else:
                diffs += 1
        if diffs == 1:
            return True
        else:
            return False

    def get_shared_letters(self, other):
        return_str = ""
        for i in range(len(self.code)):
            if self.code[i] == other.code[i]:
                return_str += self.code[i]
            else:
                pass
        return return_str


def get_boxlist_checksum(boxlist):
    doublecount = len([x for x in boxlist if x.hasdouble])
    triplecount = len([x for x in boxlist if x.hastriple])
    return doublecount * triplecount


def get_first_matching_boxes(boxlist):
    for i, j in combinations(boxlist, 2):
        if i == j:
            return (i, j)
    return None


if __name__ == '__main__':
    teststrings = [
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabcdd',
        'abcdee',
        'ababab'
    ]
    testboxlist = []
    for i in teststrings:
        testbox = Box(i)
        testboxlist.append(testbox)
        print(testbox.code, testbox.hasdouble, testbox.hastriple)
    print('Checksum:', get_boxlist_checksum(testboxlist))
    testboxes = [
        Box("abcde"),
        Box("fghij"),
        Box("klmno"),
        Box("pqrst"),
        Box("fguij"),
        Box("axcye"),
        Box("wvxyz")
    ]
    matches = get_first_matching_boxes(testboxes)
    print("Matches:", matches[0].code, matches[1].code)
    sharedletters = matches[0].get_shared_letters(matches[1])
    print("Shared letters:", sharedletters)
