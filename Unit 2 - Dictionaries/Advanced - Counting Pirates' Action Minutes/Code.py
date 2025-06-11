def counting_pirates_action_minutes(logs, k):
    timeMap = {}
    res = [0]*k

    for log in logs:
        if log[0] not in timeMap:
            timeMap[log[0]] = {log[1]}
        else:
            timeMap[log[0]].add(log[1])

    for sets in timeMap.values():
        res[len(sets)-1] += 1
    
    return res

logs1 = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k1 = 5
logs2 = [[1, 1], [2, 2], [2, 3]]
k2 = 4
print(counting_pirates_action_minutes(logs1, k1)) 
print(counting_pirates_action_minutes(logs2, k2))