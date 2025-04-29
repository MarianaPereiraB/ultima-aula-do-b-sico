a = [1,2,3,4,5]
M = [0]*5
x = int(input("digite um número: "))
for u in range (len(a)):
    M[u] = a[u]*x
print(M)