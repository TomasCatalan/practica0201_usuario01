x = float(input("Introduzca un numero en euros"))
(y) = round(x, 2)
z = str(y)

a = z.split(".")

print("El precio son", a[0], "euros y", a[1], "centimos")