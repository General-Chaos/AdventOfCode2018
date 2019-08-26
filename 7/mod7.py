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


def worker_time(events, offset, worker_count):
    workers = dict()
    for i in range(worker_count):
        workers.update({i: {'target': None, 'timer': None}})
    time = 0
    while len(events.keys()) > 0:
        # Clear any keys that have completed and count down
        for v in workers.values():
            if v['target'] is None:
                pass
            else:
                if v['timer'] == 1:
                    del events[v['target']]
                    for j in events.values():
                        j.discard(v['target'])
                    v['target'] = None
                else:
                    v['timer'] -= 1
        # fill up workers
        for v in workers.values():
            current_targets = [x['target'] for x in workers.values()]
            avaliable_targets = [x for x in events.keys() if len(events[x]) == 0]
            valid_targets = [x for x in avaliable_targets if x not in current_targets]
            if v['target'] is None:
                if len(valid_targets) > 0:
                    v['target'] = valid_targets[0]
                    v['timer'] = ord(valid_targets[0]) - 64 + offset
        if len(events.keys()) > 0:
            time += 1
        else:
            pass
    return time


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
    parsed = parse_input(input_strings)
    print(worker_time(parsed, 0, 2))
