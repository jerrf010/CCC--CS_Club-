n = int(input())

days = []
i = 0
consecutive = 0
left = ""
final = 0

for _ in range(n):
    days.append(str(input()))

for i in range(n):
    if days[i] == 'S':
        consecutive += 1
    else:
        if days[i] == 'P' and i !=0:
            if days[i + 1] == 'S' and days[i - 1] == 'S':
                consecutive += 1
                done = True
            else:
                consecutive = 0
        else:
            consecutive = 0
    if consecutive > final:
        final = consecutive

print(final)