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
    re_freeze = False
    for i in range(n-2, -1, -1):
        if -1 in city_t[i]: # -1 is for X and -2 is for O
            re_freeze = True
        for j in range(m):
            if city_t[i][j] == -1:
                dp[i][j] = 0
            elif city_t[i][j] == -2 or not re_freeze:
                mv1 = (dp[i+1][j-1]-1, j-1) if j else (0, j)
                mv2 = (dp[i+1][j]+1, j)
                mv3 = (dp[i+1][j+1]-1, j+1) if j != (m-1) else (0, j)
                temp = max(mv1, mv2, mv3, key=lambda x:x[0])
                dp[i][j] = 0 if city_t[i][j] == -2 else city_t[i][j] 
                dp[i][j] += temp[0]
                re_freeze = False

                # Storing path in a parent matrix (Time efficient)
                parent[i][j] = temp[1] if temp else -1

    start_point = max(range(m), key=lambda j: dp[0][j])
    path = [start_point]
    pos = start_point
    for row in parent[:-1]:
        # print(pos)
        pos = row[pos]
        path.append(pos)


    return (max(dp[0]), path)
    # return (dp, path)


def main():
    n, m = [int(i) for i in input().split()]

    city = [[] for _ in range(n)]

    for i in range(n):
        populations = [int(p) if (p != 'X' and p != 'O') else -1 if p != 'O' else -2 for p in input().split()]
        city[i].extend(populations)

    city_t = transpose(city)



    result = happiness(city_t)

    # for row in result[0]:
    #     print(row)

    print(result[0])
    print(' '.join(str(i) for i in result[1]))


if __name__ == "__main__":
    main()