
#Inicio Python

nombre = "carlos"

print(nombre)

#tipo de dato
print("tipo", type(nombre))

#metodos en variables

print(nombre.upper())

#apellido

apellido: str="Soto"
print(apellido, type(apellido))

#posicion de memoria

print(id(apellido))

numeroentero_1 =10
numeroentero_2 =20
print(numeroentero_1 / numeroentero_2)
print(numeroentero_1 + numeroentero_2)
print(numeroentero_1 - numeroentero_2)
print(numeroentero_1 * numeroentero_2)
print("Division", 7/2 , type(7/2))
print("Division (int)", 7//2 , type(7//2))

#Resto de la division
print("Division (modulo)", 7%2 , type(7%2))
print("Division", 2%2 , type(2%2))

#caso de uso

elementos = 33
paginas = 10
print("tenemos", elementos // paginas, "paginas")


if (10 % 2) == 0:
    print("el numero es par")
else:
    print("el numero es impar")  

#comportamiento de cadena de texto

ciudad =  "La Serena", type(str)
av_n = 10, type(str)
print( ciudad + av_n )

n1 = 10
n2 = 20
print(n1 + n2)

#Otros

print()
primer_numero = input("Ingrese el primer numero")
segundo_numero = input("Ingrese el segundo numero")

#concatenar (son string (str))
print("la suma de esta es:", primer_numero +segundo_numero)

#conversion
print("la suma de esta es:", int(primer_numero) + int(segundo_numero))

#usando f-string}
print(
    f"la suma de {primer_numero} con {segundo_numero} es: {int(primer_numero) + int(segundo_numero)}" 
)

suma = f"la suma de {primer_numero} con {segundo_numero} es: {int(primer_numero) + int(segundo_numero)}"

print(suma)