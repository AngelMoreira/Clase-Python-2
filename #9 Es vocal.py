letra = input("Ingrese una letra: ")
if len(letra) > 1:
    print("Sólo debe ingresar una letra")
else:
    if letra.lower() in ("a", "e", "i", "o", "u"):
        print("Es vocal")
    else:
        print("No es vocal")
