num = int(input())
word = str(input())

if word.count("A") < word.count("B"):
    print("B")

elif word.count("A") > word.count("B"):
    print("A")

else:
    print("Tie")