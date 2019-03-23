import sys
import copy


# I wrote this as a recursive function but it broke the recursion depth:)
def pair_destroy(compound: str):
    result = ''
    old_result = compound
    while len(old_result) != len(result):
        old_result = copy.copy(result)
        result = ''
        skip_next = False
        len_compound = len(compound) - 1
        for i, c in enumerate(compound):
            if not (i == len_compound):
                if not skip_next:
                    if c.istitle():
                        if compound[i+1] == c.lower():
                            skip_next = True
                        else:
                            result += c
                    else:
                        if compound[i+1] == c.upper():
                            skip_next = True
                        else:
                            result += c
                else:
                    skip_next = False
            else:
                result += c
        compound = result
    return result


def shortest_remove_type(compound):
    results = list()
    for i in range(97, 123):
        new_compound = (compound.replace(chr(i), "")).replace(chr(i).upper(), "")
        min_length = len(pair_destroy(new_compound))
        results.append((chr(i), min_length))

    return sorted(results, key=lambda x: x[1])[0]


if __name__ == '__main__':
    result = pair_destroy('dabAcCaCBAcCcaDA')
    print(result)
    print(shortest_remove_type('dabAcCaCBAcCcaDA'))
