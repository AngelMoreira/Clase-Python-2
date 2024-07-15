valor_decimal = float(input("Ingrese el valor en decimales: "))
iva = valor_decimal * 0.15
valor_total = valor_decimal + iva
print(f"El valor total con IVA incluido es: {valor_total:.2f}")
