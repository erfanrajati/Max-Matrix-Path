n, m = [int(i) for i in input().split()]

city = [[] for _ in range(n)]

for i in range(n):
    populations = [int(p) for p in input().split()]
    city[i].extend(populations)

# for i in city:
#     print(i)

# Transpose the matrix

from transpose import transpose

city_t = transpose(city)



path = []
happiness = 0
start_point = city_t[0].index(max(city_t[0]))
path.append(start_point)
happiness += city_t[0][start_point]

pos = start_point
for i, row in enumerate(city_t[1:]):
    if pos != 0:
        target = (max(row[pos-1:pos+2]))
        pos = row.index(target, pos-1, pos+2)
    else:
        target = (max(row[0:pos+2]))
        pos = row.index(target, 0, pos+2)

    path.append(pos)
    happiness += row[pos]


print(happiness)
print(' '.join(str(i) for i in path))