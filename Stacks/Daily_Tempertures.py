def daily_temp(Temperatures):
    n = len(Temperatures)
    res = [0] * n
    stack = []

    for i, t in enumerate(Temperatures):
        while stack and t > Temperatures[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev
        
        stack.append(i)
    return res

print(daily_temp([30,38,30,36,35,40,28]))