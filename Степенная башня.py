import sympy
m = 10**50
a = 2017
phi1 = {}
for i in range(0,2000):
    m= sympy.totient(m)
    phi1[i] = m

phi = {}
for i in range(0,2000):
    phi[i] = phi1[1999-i]

ans = 0
for i in range(1849,1999):
    ans = a%phi[i]
    print(phi[i], ans)
    ans = pow(a,ans,phi[i+1])
    print(ans)
    input()

ans = pow(a,ans,10**50)
print(ans)
