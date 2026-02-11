path = []
n = 3


def backtrack(remaining):
    if remaining == 0:
        print(path)
        return
    if remaining < 0:
        return
    
    path.append(1)
    backtrack(remaining - 1)

    path.pop()

    path.append(2)
    backtrack(remaining - 2)

    path.pop()