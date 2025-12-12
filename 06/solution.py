from functools import reduce
ans1 = 0
ans2 = 0

with open('input', 'r') as f:
    data = []
    lines = []
    for line in f:
        line = line.strip('\n')
        lines.append(line)
        data.append(line.split())
    dlen = len(data[0])
    for i in range(dlen):
        nums = []
        for j in range(len(data) - 1):
            nums.append(int(data[j][i]))
        if data[-1][i] == '+':
            ans1 += reduce(lambda x, y: x + y, nums)
        else:
            ans1 += reduce(lambda x, y: x * y, nums)
    op = ''
    llen = max(len(line) for line in lines)
    for i in range(len(lines)):
        lines[i] += ' ' * (llen - len(lines[i]))
    nums = []
    for i in range(llen):
        num = ''
        if lines[-1][i] == '+':
            op = '+'
        elif lines[-1][i] == '*':
            op = '*'
        for j in range(len(lines) - 1):
            if lines[j][i] != ' ':
                num += lines[j][i]
        if num == '':
            if op == '+':
                ans2 += reduce(lambda x, y: x + y, nums)
            else:
                ans2 += reduce(lambda x, y: x * y, nums)
            nums = []
        else:
            nums.append(int(num))
    if op == '+':
        ans2 += reduce(lambda x, y: x + y, nums)
    else:
        ans2 += reduce(lambda x, y: x * y, nums)

print(ans1)
print(ans2)