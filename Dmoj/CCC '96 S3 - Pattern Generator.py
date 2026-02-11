current = ""

def generate(n, chars, ones_needed, current):
    if chars == n and ones_needed == 0:
        print(current)
        return
    
    if ones_needed > 0:
        generate(n, chars + 1, ones_needed - 1, current + "1")
    if n - chars > ones_needed:
        generate(n, chars + 1, ones_needed, current + "0")


no = int(input())

for i in range(no):
    n, k = input().split()
    n,k = int(n), int(k)
    print("The bit patterns are")
    generate(n, 0, k, current)