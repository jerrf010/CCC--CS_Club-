n = int(input("Enter N: "))
k = int(input("Enter K: "))

total = 0 
current_value = n

for i in range(k + 1):
    total += current_value
    current_value *= 10

print(total)