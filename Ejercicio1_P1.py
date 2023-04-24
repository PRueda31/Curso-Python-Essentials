print("Empezando a trabajar con Python")
print("Realizado por: Paúl Rueda")
print("\n\nConsultando los tipos de valores:\n\n")
v1=875
print(f"El tipo de dato {v1} es: ")
print(type(v1))

v2=4.89
print(f"\nEl tipo de dato {v2} es: ")
print(type(v2))

str1="Now is better than ever."
print(f"\nEl tipo de dato del texto: {str1} es: ")
print(type(str1))

v3=1.32
print(f"\nEl tipo de dato {v3} es: ")
print(type(v3))

c1=5+8j
print(f"\n¿El valor {c1} corresponde a un valor entero?")
print(isinstance(c1,int))

v4=8.2
print(f"\n¿El valor {v4} corresponde a un valor entero?")
print(isinstance(v4,int))

str2="Readability counts."
print(f"\n¿El texto {str2} corresponde a string?")
print(isinstance(str2,str))
