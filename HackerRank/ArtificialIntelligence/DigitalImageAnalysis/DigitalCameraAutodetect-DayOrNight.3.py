row_s = input().strip()
grid = []

while row_s is not None and row_s != "":
    grid.append([sum([int(val_s) for val_s in pxl_s.split(",")]) for pxl_s in row_s.split(" ")])
    try:
        row_s = input().strip()
    except EOFError:
        break

height = len(grid)
width = len(grid[0])

avg = sum([sum(row) for row in grid]) / (height * width)
print('day' if avg > 255 else 'night')
