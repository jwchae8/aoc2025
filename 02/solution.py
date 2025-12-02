ans1 = 0
ans2 = 0
with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        ranges = line.split(',')
        for r in ranges:
            start, end = r.split('-')
            start = int(start)
            end = int(end)
            for i in range(start, end+1):
                str_i = str(i)
                str_len = len(str_i)
                if str_len % 2 == 0:
                    if str_i[:str_len // 2] == str_i[str_len // 2:]:
                        ans1 += i
                for j in range(str_len // 2):
                    if str_len % (j + 1) == 0:
                        nom = int(('0' * j + '1') * (str_len // (j + 1)))
                        if i % nom == 0 and nom * nom > i:
                            ans2 += i
                            break

# Answer of part1 is 5398419778
print(ans1)

# Answer of part2 is 15704845910
print(ans2)