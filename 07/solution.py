ans = 0
with open('input', 'r') as f:
    beam = set()
    routes = {}
    for line in f:
        line = line.strip()
        for i, c in enumerate(line):
            if c == 'S':
                beam.add(i)
                routes[i] = 1
            elif c == '^' and i in beam:
                beam.add(i - 1)
                beam.add(i + 1)
                beam.remove(i)
                if i - 1 >= 0:
                    routes[i - 1] = routes.get(i - 1, 0) + routes[i]
                if i + 1 < len(line):
                    routes[i + 1] = routes.get(i + 1, 0) + routes[i]
                routes[i] = 0
                ans += 1
print(ans)
print(sum(routes.values()))