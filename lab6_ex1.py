def mult(a=0, n=0):
    a = int(input())
    n = int(input())
    for i in range(n-1):
        a *= a
    return a
print(mult())

