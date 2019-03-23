import re


# plan is to normalise to smallest area, then assume that any that have closest points on the edges have infinite areeas
def parse_and_normalise(input):
    coords = dict()
    for i in input:
        matches = re.match(r"(\d+), (\d+)", i)
        coords.update({i: {'x': int(matches.group(1)), 'y': int(matches.group(2)), 'closest': 0, 'infinite': False}})
    min_x = min([x['x'] for x in coords.values()])
    min_y = min([x['y'] for x in coords.values()])
    for c in coords.keys():
        coords[c]['x'] -= min_x
        coords[c]['y'] -= min_y
    return coords


def update_closest(x, y, places, mark_infinite=False):
    current_min = None
    closest_place = list()
    for k, v in places.items():
        dist = abs(x - v['x']) + abs(y - v['y'])
        if current_min is not None:
            if dist < current_min:
                current_min = dist
                closest_place = [k]
            elif dist == current_min:
                closest_place.append(k)
            else:
                pass
        else:
            current_min = dist
            closest_place = [k]
    if len(closest_place) == 1:
        places[closest_place[0]]['closest'] += 1
        if mark_infinite:
            places[closest_place[0]]['infinite'] = True
        else:
            pass
    else:
        pass


def get_largest_area(input):
    parsed_input = parse_and_normalise(input)
    max_x = max([x['x'] for x in parsed_input.values()])
    max_y = max([x['y'] for x in parsed_input.values()])
    # go along the edges and mark the closest points as infinite
    for i in range(max_x + 1):
        update_closest(i, 0, parsed_input, True)
        update_closest(i, max_y, parsed_input, True)
    for i in range(max_y + 1):
        update_closest(0, i, parsed_input, True)
        update_closest(max_x, i, parsed_input, True)
    # iterate over the interior
    for i in range(1, max_x):
        for j in range(1, max_y):
            update_closest(i, j, parsed_input)
    # Find the largest non infinite area
    sortedx = sorted([x['closest'] for x in parsed_input.values() if not x['infinite']], reverse=True)
    return sortedx[0]


def get_area_under_dist(input, distance):
    parsed_input = parse_and_normalise(input)
    max_x = max([x['x'] for x in parsed_input.values()])
    max_y = max([x['y'] for x in parsed_input.values()])
    within = 0
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            dist = 0
            for v in parsed_input.values():
                dist += abs(i - v['x']) + abs(j - v['y'])
            if dist < distance:
                within += 1
    return within


if __name__ == '__main__':
    problem_input = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]
    parsed_input = parse_and_normalise(problem_input)
    print(parsed_input)
    max_area = get_largest_area(problem_input)
    print(max_area)
