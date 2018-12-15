import re
from datetime import datetime


def parse_log_line(line: str):
    matches = re.match(r"\[(.*)\] (.*)", line)
    ret = {}
    ret["date"] = datetime.strptime(matches.group(1), r"%Y-%m-%d %H:%M")
    ret["Event"] = matches.group(2)
    return ret


def process_event_stream(events):
    guard_data = {}
    sorted_stream = sorted(events, key=lambda x: x['date'])
    for event in sorted_stream:
        if re.match("Guard", event['Event']):
            match = re.match(r"Guard #(\d+) begins shift", event['Event'])
            current_guard = match.group(1)
        elif re.match("falls asleep", event['Event']):
            start_sleep = event['date'].minute
        elif re.match("wakes up", event['Event']):
            end_sleep = event['date'].minute
            guard_data.setdefault(current_guard, {})
            for i in range(start_sleep, (end_sleep + 1)):
                guard_data[current_guard].setdefault(i, 0)
                guard_data[current_guard][i] += 1
    return guard_data


def get_most_slept(guard_data):
    most_slept = sorted(list(guard_data.items()), key=lambda x: sum(x[1].values()), reverse=True)[0]
    guard = {}
    guard['id'] = int(most_slept[0])
    guard['most_slept_min'] = sorted(list(most_slept[1].items()), key=lambda x: x[1], reverse=True)[0][0]
    return guard


def get_max_min_slept(guard_data):
    most_slept = sorted(list(guard_data.items()), key=lambda x: max(x[1].values()), reverse=True)[0]
    guard = {}
    guard['id'] = int(most_slept[0])
    guard['most_slept_min'] = sorted(list(most_slept[1].items()), key=lambda x: x[1], reverse=True)[0][0]
    return guard


if __name__ == "__main__":
    logparse = parse_log_line("[1518-03-22 23:52] Guard #617 begins shift")
    print(logparse)
