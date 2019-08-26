import os
import re


def parse_input(input_strings):
    results = list()
    regex = r"\w+=<\s*(-*\d+),\s*(-*\d+)> velocity=<\s*(-*\d+),\s*(-*\d+)>"
    for i in input_strings:
        match = re.match(regex, i)
        results.append({
            'x': int(match.group(1)),
            'y': int(match.group(2)),
            'dx': int(match.group(3)),
            'dy': int(match.group(4))
        })
    return results


def proc_time(lights, forward=True):
    if forward:
        for i in lights:
            i['x'] += i['dx']
            i['y'] += i['dy']
    else:
        for i in lights:
            i['x'] -= i['dx']
            i['y'] -= i['dy']


def get_mins(lights):
    x = [x['x'] for x in lights]
    y = [x['y'] for x in lights]
    result = {
        'x': max(x) - min(x),
        'y': max(y) - min(y)
    }
    return result


def find_y_minima(lights):
    seconds = 0
    minima_found = False
    current_min = get_mins(lights)['y']
    while not minima_found:
        seconds += 1
        proc_time(lights)
        new_min = get_mins(lights)['y']
        if new_min > current_min:
            seconds -= 1
            minima_found = True
            proc_time(lights, False)
            return [lights, seconds]
        else:
            current_min = new_min


def output_file(lights, filename):

    # normalize
    min_x = min([x['x'] for x in lights])
    min_y = min([x['y'] for x in lights])
    for i in lights:
        i['x'] -= min_x
        i['y'] -= min_y
    max_x = max([x['x'] for x in lights])
    max_y = max([x['y'] for x in lights])
    # create arrays back to front
    output = []
    for i in range(max_y + 1):
        output.append(['.'] * (max_x + 1))
    for i in lights:
        output[i['y']][i['x']] = '#'
    with open(filename, 'w') as f:
        for i in output:
            f.writelines(''.join(i) + '\n')


if __name__ == "__main__":
    input_strings = [
        "position=< 9,  1> velocity=< 0,  2>",
        "position=< 7,  0> velocity=<-1,  0>",
        "position=< 3, -2> velocity=<-1,  1>",
        "position=< 6, 10> velocity=<-2, -1>",
        "position=< 2, -4> velocity=< 2,  2>",
        "position=<-6, 10> velocity=< 2, -2>",
        "position=< 1,  8> velocity=< 1, -1>",
        "position=< 1,  7> velocity=< 1,  0>",
        "position=<-3, 11> velocity=< 1, -2>",
        "position=< 7,  6> velocity=<-1, -1>",
        "position=<-2,  3> velocity=< 1,  0>",
        "position=<-4,  3> velocity=< 2,  0>",
        "position=<10, -3> velocity=<-1,  1>",
        "position=< 5, 11> velocity=< 1, -2>",
        "position=< 4,  7> velocity=< 0, -1>",
        "position=< 8, -2> velocity=< 0,  1>",
        "position=<15,  0> velocity=<-2,  0>",
        "position=< 1,  6> velocity=< 1,  0>",
        "position=< 8,  9> velocity=< 0, -1>",
        "position=< 3,  3> velocity=<-1,  1>",
        "position=< 0,  5> velocity=< 0, -1>",
        "position=<-2,  2> velocity=< 2,  0>",
        "position=< 5, -2> velocity=< 1,  2>",
        "position=< 1,  4> velocity=< 2,  1>",
        "position=<-2,  7> velocity=< 2, -2>",
        "position=< 3,  6> velocity=<-1, -1>",
        "position=< 5,  0> velocity=< 1,  0>",
        "position=<-6,  0> velocity=< 2,  0>",
        "position=< 5,  9> velocity=< 1, -2>",
        "position=<14,  7> velocity=<-2,  0>",
        "position=<-3,  6> velocity=< 2, -1>"
    ]

    parsed = parse_input(input_strings)

    fileDir = os.path.dirname(os.path.realpath(__file__))
    testfile = os.path.join(fileDir, 'test.txt')
    min_parsed = find_y_minima(parsed)
    output_file(min_parsed[0], testfile)
    print(f"Seconds: {min_parsed[1]}")
