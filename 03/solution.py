ans1 = 0
ans2 = 0

with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        digits = len(line)
        left = 0
        for i in range(digits - 1):
            if line[left] < line[i]:
                left = i
        right = left + 1
        for i in range(left + 1, digits):
            if line[right] < line[i]:
                right = i
        ans1 += int(line[left] + line[right])
        twelves = ''
        idx = 0
        for i in range(11, -1, -1):
            for j in range(idx, digits - i):
                if line[idx] < line[j]:
                    idx = j
            twelves += line[idx]
            idx += 1
        ans2 += int(twelves)

# Answer of part1 is 17142
print(ans1)

# Answer of part2 is 169935154100102
print(ans2)