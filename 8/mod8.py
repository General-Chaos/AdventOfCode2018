

def process_license(numbers):
    child_nodes = numbers[0]
    meta_data_count = numbers[1]
    children = list()
    numbers = numbers[2:]
    for _ in range(child_nodes):
        result = process_license(numbers)
        numbers = result[0]
        children += result[1]
    result = list()
    result.append({
        'metadata': numbers[:(meta_data_count)],
        'children': children[:]
    })
    numbers = numbers[(meta_data_count):]
    return [numbers, result]


def yield_metadata(license_file):
    for i in license_file['children']:
        yield from yield_metadata(i)
    for i in license_file['metadata']:
        yield i


def yield_node_values(license_file):
    if len(license_file['children']) == 0:
        yield sum(license_file['metadata'])
    else:
        child_count = len(license_file['children'])
        for i in license_file['metadata']:
            if i > child_count:
                yield 0
            else:
                yield from yield_node_values(license_file['children'][(i-1)])


def get_root_node_value(license_file):
    return sum(yield_node_values(license_file))


if __name__ == "__main__":
    test = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    license_file = (process_license(test))[1][0]
    print(license_file)
    print(sum(yield_metadata(license_file)))
    print(get_root_node_value(license_file))
