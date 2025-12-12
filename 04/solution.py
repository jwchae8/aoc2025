directions = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 0), (-1, -1), (-1, 1)]
grid = []
ans1 = 0
ans2 = 0

with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        grid.append(list(line))
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '.':
                continue
            cnt = 0
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
                    continue
                if grid[newRow][newCol] == '@':
                    cnt += 1
            if cnt < 4:
                ans1 += 1
    prev_ans2 = None
    while prev_ans2 != ans2:
        prev_ans2 = ans2
        removed = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '.':
                    continue
                cnt = 0
                for direction in directions:
                    newRow = row + direction[0]
                    newCol = col + direction[1]
                    if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
                        continue
                    if grid[newRow][newCol] == '@':
                        cnt += 1
                if cnt < 4:
                    ans2 += 1
                    removed.append((row, col))
        for row, col in removed:
            grid[row][col] = '.'


print(ans1)
print(ans2)
