n = int(input())

for _ in range(n):
    code = input()
    letters = ""
    total = 0
    i = 0

    while i < len(code):
        if code[i].isupper():
            letters += code[i]
            i += 1

        elif code[i] == '-' or code[i].isdigit():
            start = i
            if code[i] == '-':
                i += 1
            while i < len(code) and code[i].isdigit():
                i += 1
            total += int(code[start:i])

        else:
            i += 1

    print(letters + str(total))
