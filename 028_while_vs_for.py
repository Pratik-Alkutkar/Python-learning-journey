
i = 0
while i < N:
    UPPER HALF
    if cond:
        i = i + 1
        continue
    LOWER HALF
    i=i+1

for x in L:
    if x % 10 == 0:
        continue
    print(x)

i = 0
while i < len(L):
    if L[i] % 10 == 0:
        i = i + 1
        continue
    print(L[i])
    i= i + 1 