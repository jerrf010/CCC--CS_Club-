d  = int(input("Number of donuts: "))
e = int(input("Number of events: "))
q = 0
for i in range(e):
    q = int(input("Donuts in event: "))
    i = (input("- or +: \n"))
    if i == "+":
        q += d
    elif i == "-":
        q -= d
r = q
if r < 0:
    print("0")
else:
    print(r)