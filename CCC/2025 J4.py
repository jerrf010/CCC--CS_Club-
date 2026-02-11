n = int(input())

days = []
i = 0
consecutive = 0
left = ""
done = False
final = 0

for _ in range(n):
    days.append(str(input()))

for i in range(n):
    if days[i] == 'S':
        consecutive += 1
    else:
        if days[i] == 'P':
            if days[i + 1] == 'S' and not done:
                consecutive += 1
                done = True
            else:
                consecutive = 0
    if consecutive > final:
        final = consecutive

print(consecutive)