alice = [1, 2, 3]
bob = [3, 2, 1]

results = [0, 0]

for i in range(0, 3):  
    if alice[i] < bob[i]:
        results[1] += 1
    elif alice[i] > bob[i]:
        results[0] += 1


print(results)