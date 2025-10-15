n = int(input("Enter a number: "))
operations = 0
while n != 1:
    if n%2==0:
        n = n/2
        print(n)
        operations += 1
    else:
        n = n*3
        n = n+1
        print(n)
        operations += 1
print("Total operations: " + str(operations))