x = input("Introduzca el nombre del producto")
y = float(input("Introduzca el precio unitario"))
z = int(input("Introduzca el numero de unidades"))

a = round(y, 2)
b = round((a * z), 2)

print("El producto", x, "con un precio unitario de", y, "y", z,
    "unidades,tendra un coste total de", b, "euros")