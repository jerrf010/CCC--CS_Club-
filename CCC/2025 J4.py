n = int(input())
days = [input().strip() for _ in range(n)]

max_streak = 0
left = 0
p_count = 0

for right in range(n):
    if days[right] == 'P':
        p_count += 1

    while p_count > 1:
        if days[left] == 'P':
            p_count -= 1
        left += 1

    max_streak = max(max_streak, right - left + 1)

print(max_streak)
