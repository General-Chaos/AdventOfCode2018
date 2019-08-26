import mod11

grid1 = mod11.generate_grid(300, 3031)
answer1 = mod11.get_best_grid(grid1, 3)
print(f"The answer to day 11 part 1 is: {answer1['x']},{answer1['y']}")

answer2 = mod11.get_best_grid_size(grid1, 300)
print(f"The answer to day 11 part 1 is: {answer2['x']},{answer2['y']},{answer2['size']}")
