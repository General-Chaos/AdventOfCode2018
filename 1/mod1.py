from copy import copy


def get_offsets(starting_offset, instructions):
    next_offset = copy(starting_offset)
    for i in instructions:
        next_offset += i
        yield next_offset


def get_first_repeat(starting_offset, instructions, seen=set()):
    for i in get_offsets(starting_offset, instructions):
        if i in seen:
            return i
        else:
            seen.add(i)
    return get_first_repeat(i, instructions, seen=seen)
