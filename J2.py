d  = int(input("Number of donuts: "))
e = int(input("Number of events: "))
q = 0
for i in range(e):
    track = input("+ or -: \n")
    if track == "+":
        i = int(input("Number of donuts added: "))
    if track == "-":
        i = int(input("Number of donuts sold: "))
        i = -i
    q += i

r = q + d
if r < 0:
    print("0")
else:
    print(r)