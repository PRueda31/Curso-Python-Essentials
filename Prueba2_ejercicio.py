print("\nMenú de programas activos")
print("\n1) Programa para identificar el tipo de datos de un conjunto dado. \
      \n2) Programa para identificar el tipo de datos ingresados por el usuario. \
      \n3) Programa para identificar números pares e impares de una lista. \
      \n4) Programa para verificar que una contraseña cumpla con ciertos requisitos. \
      \n5) Programa para identificar valores altos y bajos en un diccionario.")
# a=int(input("\nIngrese la opción del programa que desea llamar: "))

try:
    a=int(input("\nIngrese la opción del programa que desea llamar: "))
    
    if a>=1 and a<=5:
        if a==1:
            import Ejercicio1_P1 
        elif a==2:
            import Datosusuario
        elif a==3:
            import Ejercicio2_P1
        elif a==4:
            import verpass
        elif a==5:
            import Ejercicio3
    else:
        print("La opción escogida no se encuentra disponible en el menú.")
except:
    print("\nLa opción ingresada no coincide con el menú disponible. Tome en cuenta que \
solo puede ingresar el número de opción como un número entero.")

    
