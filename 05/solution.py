ranges = []
ingredients = []
ans1 = 0
ans2 = 0

with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        if '-' in line:
            l, r = line.split('-')
            ranges.append([int(l), int(r)])
        elif line:
            ingredients.append(int(line))
    for ingredient in ingredients:
        for left, right in ranges:
            if left <= ingredient <= right:
                ans1 += 1
                break
    combined = []
    ranges.sort(key=lambda x: x[0])
    for range in ranges:
        if not combined or range[0] > combined[-1][1] + 1:
            combined.append(range)
        else:
            combined[-1][1] = max(combined[-1][1], range[1])
    for l, r in combined:
        ans2 += r - l + 1
print(ans1)
print(ans2)