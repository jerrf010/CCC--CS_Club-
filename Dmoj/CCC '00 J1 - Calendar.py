try:
    day, amount = input("Input the starting day, then amount of days in the month (separated by space) \n").split()
except ValueError:
    print("Invalid input. Please enter two integers separated by a space.")
    exit(1)

day = int(day)
amount = int(amount)
print()

print("Sun Mon Tue Wed Thu Fri Sat")
for i in range(day - 1):
    print("    ", end="")

for i in range(amount):
    print(f"{i+1:>3} ", end="")
    if (i + day) % 7 == 0:
        print()  
print()