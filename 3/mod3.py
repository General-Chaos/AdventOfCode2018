import re


class Fabric():

    def __init__(self, x_length: int, y_length: int):
        self.fabric = [[[] for i in range(y_length)] for i in range(x_length)]

    def add_claim(self, claim_str: str):
        matches = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", claim_str)
        claim_id = int(matches.group(1))
        x_start = int(matches.group(2))
        x_end = int(matches.group(2)) + int(matches.group(4))
        y_start = int(matches.group(3))
        y_end = int(matches.group(3)) + int(matches.group(5))
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                self.fabric[i][j].append(claim_id)

    def __repr__(self):
        string = ""
        for i in range(len(self.fabric)):
            string += f"{self.fabric[i].__str__()}\n"
        return string

    def get_overclaimed_area(self):
        overprovisioned = 0
        for i in range(len(self.fabric)):
            for j in range(len(self.fabric[1])):
                if len(self.fabric[i][j]) > 1:
                    overprovisioned += 1
        return overprovisioned

    def get_first_nooverlap(self):
        seen_set = set()
        overlap_set = set()
        for i in range(len(self.fabric)):
            for j in range(len(self.fabric[1])):
                if len(self.fabric[i][j]) > 1:
                    for k in self.fabric[i][j]:
                        overlap_set.add(k)
                        seen_set.add(k)
                elif len(self.fabric[i][j]) == 1:
                    seen_set.add(self.fabric[i][j][0])
        return [x for x in seen_set if x not in overlap_set][0]


if __name__ == "__main__":
    testfabric = Fabric(8, 8)
    claims = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2"
    ]
    for i in claims:
        testfabric.add_claim(i)
    print(testfabric)
    print(testfabric.get_overclaimed_area())
    print(testfabric.get_first_nooverlap())
