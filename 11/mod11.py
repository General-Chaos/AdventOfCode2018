def get_power_level(x_val, y_val, serial_number):
    rack_id = x_val + 10
    power = rack_id * y_val
    power = power + serial_number
    power = power * rack_id
    power = [int(x) for x in str(power)]
    if len(power) > 2:
        power = power[-3]
    else:
        power = 0
    power -= 5
    return power


def generate_grid(total_size, serial_number):
    grid = list()
    for i in range(total_size):
        grid.append([])
        for j in range(total_size):
            grid[i].append(get_power_level(i, j, serial_number))
    return grid


def get_best_grid(grid, grid_size):
    big_list = []
    for i in range(len(grid)-grid_size + 1):
        for j in range(len(grid[i]) - grid_size + 1):
            grid_sum = 0
            for k in range(grid_size):
                grid_sum += sum(grid[i+k][j:j+grid_size])
#                for l in range(grid_size):
#                    grid_sum += grid[i+k][j+l]['power']
            big_list.append({
                'x': i,
                'y': j,
                'grid_power': grid_sum,
                'size': grid_size
            })
    sorted_list = sorted(big_list, key=lambda x: x['grid_power'], reverse=True)
    return sorted_list[0]


def get_best_grid_size(grid, max_grid_size):
    results = []
    for i in range(1, max_grid_size):
        best = get_best_grid(grid, i)
        results.append(best)
    result = sorted(results, key=lambda x: x['grid_power'], reverse=True)[0]
    return result


if __name__ == "__main__":
    grid = generate_grid(300, 18)
    print(get_best_grid(grid, 3))
    grid = generate_grid(300, 42)
    print(get_best_grid(grid, 3))
    print(get_best_grid_size(grid, 300))
