n = int(input())
days = [input().strip() for _ in range(n)]
max_streak = 0
left = 0
b_count = 0

for i in range(n):
    if days[i] == 'B':
        b_count += 1
    while b_count > 1:
        if days[left] == 'B':
            b_count -= 1
        left += 1
    max_streak = max(max_streak, i - left + 1)
print(max_streak)