nombre = "Felipe"
edad = 23
altura = 1.75
es_estudiante = True
nombreMadre = "Liliana"
edadMadre = 45
alturaMadre = 1.60

suma = edad + edadMadre
resta = altura - alturaMadre
multiplicacion = edad * 2
division = altura / 2

print("El se llama:", nombre)
print("Tiene:", edad, "años")

if edad >= 18:
    print(f"{nombre} es mayor de edad.")
else:
    print(f"{nombre} es menor de edad.")

if es_estudiante == True:
    print("Es estudiante.")
else:
    print("No es estudiante.")


print("Mide:", altura, "metros")
print("La suma de las edades de la madre y Felipe es de", suma)
print("La diferencia de la altura de Felipe y la madre es", resta)
print("El doble de la edad de Felipe es:", multiplicacion)
print("La mitad de la altura de Felipe es:", division)

print("Contando hasta 5:")
for i in range(1, 6):
    print(i)

contador = 0
print("Contando hasta 3 con bucle while:")
while contador < 3:
    print(contador)
    contador += 1