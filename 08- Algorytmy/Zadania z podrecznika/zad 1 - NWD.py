def NWD(a,b):
    if a < b:
        a,b = b,a
    while b:
        a, b = b, a % b
    return a

print(NWD(12,18))