edad = int(input("Ingrese la edad de la persona: "))
cantidad_articulos = int(input("Ingrese la cantidad de artículos comprados: "))
resultado = (edad > 18) and (cantidad_articulos > 1)
print(f"La persona es mayor de 18 años y compró más de 1 artículo: {resultado}")