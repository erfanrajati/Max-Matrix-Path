from transpose import transpose

def happiness(city_t, dp=0):
    n = len(city_t)
    m = len(city_t[0])

    dp = [[0 for _ in range(m)]for _ in range(n)]
    parent = [[-1 for _ in range(m)]for _ in range(n)]

    # base case
    for i, row in enumerate(city_t[-1]):
        dp[-1][i] = row


    # let dp[i][j] = city_t[i][j] + max(dp[i-1][j+1], dp[i][j+1], dp[i+1][j+1])
    for i in range(n-2, -1, -1):
        for j in range(m):
            # print(f"i={i}\nj={j}")
            mv1 = (dp[i+1][j-1], j-1) if j else (0, j)
            mv2 = (dp[i+1][j], j)
            mv3 = (dp[i+1][j+1], j+1) if j != (m-1) else (0, j)
            temp = max(mv1, mv2, mv3, key=lambda x:x[0])
            dp[i][j] = city_t[i][j] + temp[0]

            # Storing path in a parent matrix (Time efficient)
            parent[i][j] = temp[1]

    
    # Reconstructing the path
    for row in parent:
        print(row)

    start_point = max(range(m), key=lambda j: dp[0][j])
    path = [start_point]
    pos = start_point
    for row in parent[:-1]:
        pos = row[pos]
        path.append(pos)


    # Finding the path using greedy approach (Memory efficient)
    # greedy_path = []
    # start_point = city_t[0].index(max(city_t[0]))
    # greedy_path.append(start_point)

    # pos = start_point
    # for i, row in enumerate(city_t[1:]):
    #     if pos != 0:
    #         target = (max(row[pos-1:pos+2]))
    #         pos = row.index(target, pos-1, pos+2)
    #     else:
    #         target = (max(row[0:pos+2]))
    #         pos = row.index(target, 0, pos+2)

    #     greedy_path.append(pos)


    return (max(dp[0]), path)
    # return (max(dp[0]), greedy_path)




n, m = [int(i) for i in input().split()]

city = [[] for _ in range(n)]

for i in range(n):
    populations = [int(p) for p in input().split()]
    city[i].extend(populations)

city_t = transpose(city)



result = happiness(city_t)

# print(max(result[0][0]))

print(result[0])
print(' '.join(str(i) for i in result[1]))