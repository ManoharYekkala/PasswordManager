def minimum_colors(n, s, v):
    v.sort()
    color_count = 1
    start = v[0]
    for i in range(1, n):
        if v[i] - start > s:
            color_count += 1
            start = v[i]
    return color_count

n, s = map(int, input().strip().split())
v = map(int, input().strip().split())

print(minimum_colors(n, s, v))
