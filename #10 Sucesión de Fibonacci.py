N1 = 0
N2 = 1
print(N1)
print(N2)
for _ in range(50):
    siguiente_N = N1 + N2
    print(siguiente_N)
    N1 = N2
    N2 = siguiente_N