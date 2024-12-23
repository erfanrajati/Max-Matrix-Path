

def transpose(city):
    city_t = [[] for _ in range(len(city[0]))]
    for row in city:
        for i in range(len(row)):
            city_t[i].append(row[i])
    return city_t