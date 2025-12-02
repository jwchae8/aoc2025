ans1 = 0
ans2 = 0
pos = 50

with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        direction = line[:1]
        step = int(line[1:])
        sign = 1 if direction == 'R' else -1
        if step >= 100:
            ans2 += step // 100
            step %= 100
        next_pos = (pos + sign * step) % 100
        if next_pos == 0:
            ans1 += 1
            ans2 += 1
        elif pos == 0:
            pass
        elif (sign == 1 and next_pos < pos) or (sign == -1 and next_pos > pos):
            ans2 += 1
        pos = next_pos

# Answer of part1 is 1100
print(ans1)

# Answer of part2 is 6358
print(ans2)