def M_a_K(M):
    K = M / 1.609344
    return K
M = float(input("Ingrese el número de M: "))
K = M_a_K(M)
print(f"{M} M son equivalentes a {K} K.")