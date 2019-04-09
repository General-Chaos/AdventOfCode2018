import re


def parse_input(input_strings):
    results = dict()
    for i in input_strings:
        match = re.match(r"Step (\w) must be finished before step (\w) can begin.", i)
        if match.group(1) not in results:
            results[match.group(1)] = set()
        if match.group(2) not in results:
            results[match.group(2)] = set(match.group(1))
        else:
            results[match.group(2)].add(match.group(1))
    return results


def get_order(events):
    result = ''
    while len(events) > 0:
        # get events with no waits and order them
        next_event = sorted([x for x in events.keys() if len(events[x]) == 0])[0]
        # add event to results and remove event from all sets
        result += next_event
        del events[next_event]
        for i in events:
            events[i].discard(next_event)
    return result


if __name__ == '__main__':
    input_strings = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin."
    ]
    parsed = parse_input(input_strings)
    print(get_order(parsed))

