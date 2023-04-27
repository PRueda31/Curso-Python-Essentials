# Programa que permite identificar valores altos y bajos

print("\nPrograma que permite identificar los valores más altos y más bajos en un diccionario")
print("\n1) Demostración del cálculo de valores altos y bajos. \
      \n2) Salir.")

op=int(input("\nIngrese una opción: "))

while op!=1 and op!=2:
    op=int(input("\nERROR. Ingrese una opción válida: "))    
    
if op==2:
    print("\nFIN")

while op==1:
    if op==1:
        
        print("\n1) {'Raul': 34, 'Paula': 19, 'Jorge': 43, 'Richard': 10, 'Diana': 3 \
                    'Isabel': 76, 'Gustavo': 12, 'Diego': 37} \
              \n2) {'tplA':(4,-12,56,-34,98,102),'tplB':(9,0,1,10,-3,14),'tlpC':(87,12,56,987,-61)} \
              \n3) {'val1':-12.5,'val2':12.5,'val3':83,'val4':2.1,'val5':23,'val6':100,'val7':13.4,'val8':92} \
              \n4) {'lst1':[4,6,-12,56,-9,5.7,33,100],'lst2':[9,0,81,-2,-56,],'lst3':[12,31,87,1,0,4,-11]}")
              
        a=int(input("\nDigite la opción de diccionario con la que desea trabajar: "))
        
        d1={'Raul': 34, 'Paula': 19, 'Jorge': 43, 'Richard': 10, 'Diana': 3,
            'Isabel': 76, 'Gustavo': 12, 'Diego': 37}
        d2={'tplA':(4,-12,56,-34,98,102),'tplB':(9,0,1,10,-3,14),'tlpC':(87,12,56,987,-61)}
        d3={'val1':-12.5,'val2':12.5,'val3':83,'val4':2.1,'val5':23,'val6':100,'val7':13.4,'val8':92}
        d4={'lst1':[4,6,-12,56,-9,5.7,33,100],'lst2':[9,0,81,-2,-56,],'lst3':[12,31,87,1,0,4,-11]}
        
        n=1
        m=1
        
        # Operaciones diccionario 1
        
        ld1=len(d1)
        d1v=d1.values()
        s1=sorted(d1v)
        lis1a=[]
        lis1b=[]
        
        # Operaciones diccionario 2
        
        # Extraer los valores
        d2v=d2.values()
        s2=list(d2v)
        # Conformación de una lista en d2
        lisd2_0=list(s2[0])
        lisd2_1=list(s2[1])
        lisd2_2=list(s2[2])
        lisd2=sorted(lisd2_0+lisd2_1+lisd2_2)
        ld2=len(lisd2)
        lis2a=[]
        lis2b=[]
        
        # Operaciones diccionario 3
        
        ld3=len(d3)
        d3v=d3.values()
        s3=sorted(d3v)
        lis3a=[]
        lis3b=[]
        
        # Operaciones diccionario 4
        
        # Extraer los valores
        d4v=d4.values()
        s4=list(d4v)
        # Conformación de una lista en d4
        lisd4_0=s4[0]
        lisd4_1=s4[1]
        lisd4_2=s4[2]
        lisd4=sorted(lisd4_0+lisd4_1+lisd4_2)
        ld4=len(lisd4)
        lis4a=[]
        lis4b=[]
        
        while a!=1 and a!=2 and a!=3 and a!=4:
            a=int(input("ERROR. Ingrese una opción válida: "))
        
        if a==1:
            b=int(input("\nDigite el número de valores altos que desea mostrar: "))
            c=int(input("Digite el número de valores bajos que desea mostrar: "))
            while b>ld1 or c>ld1 or b<0 or c<0:
                print(f"\nERROR. El tamaño del arreglo es {ld1} y los valores proporcionados exceden este valor.")
                b=int(input("\nDigite el número de valores altos que desea mostrar: "))
                c=int(input("Digite el número de valores bajos que desea mostrar: "))
                
            while n<=b:
                lis1a.insert(n-1,s1[len(s1)-n])
                n=n+1
            while m<=c:
                lis1b.insert(m-1,s1[m-1])
                m=m+1
                
            print("")
            slis1a=sorted(lis1a)
            slis1b=sorted(lis1b)
            tpl1a=tuple(lis1a)
            tpl1b=tuple(lis1b)
            print(f"\nValores altos calculados en formato LISTA: {slis1a}")
            print(f"Valores altos calculados en formato TUPLA: {tpl1a}")
            print(f"\nValores bajos calculados en formato LISTA: {slis1b}")
            print(f"Valores bajos calculados en formato TUPLA: {tpl1b}")
            
        if a==2:
            b=int(input("\nDigite el número de valores altos que desea mostrar: "))
            c=int(input("Digite el número de valores bajos que desea mostrar: "))
            while b>ld2 or c>ld2 or b<0 or c<0:
                print(f"\nERROR. El tamaño del arreglo es {ld2} y los valores proporcionados exceden este valor.")
                b=int(input("\nDigite el número de valores altos que desea mostrar: "))
                c=int(input("Digite el número de valores bajos que desea mostrar: "))
                
            while n<=b:
                lis2a.insert(n-1,lisd2[len(lisd2)-n])
                n=n+1
            while m<=c:
                lis2b.insert(m-1,lisd2[m-1])
                m=m+1
                
            print("")
            slis2a=sorted(lis2a)
            slis2b=sorted(lis2b)
            tpl2a=tuple(lis2a)
            tpl2b=tuple(lis2b)
            print(f"\nValores altos calculados en formato LISTA: {slis2a}")
            print(f"Valores altos calculados en formato TUPLA: {tpl2a}")
            print(f"\nValores bajos calculados en formato LISTA: {slis2b}")
            print(f"Valores bajos calculados en formato TUPLA: {tpl2b}")
                
        if a==3:
              b=int(input("\nDigite el número de valores altos que desea mostrar: "))
              c=int(input("Digite el número de valores bajos que desea mostrar: "))
              while b>ld3 or c>ld3 or b<0 or c<0:
                  print(f"\nERROR. El tamaño del diccionario es {ld3} y los valores proporcionados exceden este valor.")
                  b=int(input("\nDigite el número de valores altos que desea mostrar: "))
                  c=int(input("Digite el número de valores bajos que desea mostrar: "))
                  
              while n<=b:
                  lis3a.insert(n-1,s3[len(s3)-n])
                  n=n+1
              while m<=c:              
                  lis3b.insert(m-1,s3[m-1])
                  m=m+1
                  
              print("")
              slis3a=sorted(lis3a)
              slis3b=sorted(lis3b)
              tpl3a=tuple(lis3a)
              tpl3b=tuple(lis3b)
              print(f"\nValores altos calculados en formato LISTA: {slis3a}")
              print(f"Valores altos calculados en formato TUPLA: {tpl3a}")
              print(f"\nValores bajos calculados en formato LISTA: {slis3b}")
              print(f"Valores bajos calculados en formato TUPLA: {tpl3b}")
              
        if a==4:
            b=int(input("\nDigite el número de valores altos que desea mostrar: "))
            c=int(input("Digite el número de valores bajos que desea mostrar: "))
            while b>ld4 or c>ld4 or b<0 or c<0:
                print(f"\nERROR. El tamaño del arreglo es {ld4} y los valores proporcionados exceden este valor.")
                b=int(input("\nDigite el número de valores altos que desea mostrar: "))
                c=int(input("Digite el número de valores bajos que desea mostrar: "))
                
            while n<=b:
                lis4a.insert(n-1,lisd4[len(lisd4)-n])
                n=n+1
            while m<=c:
                lis4b.insert(m-1,lisd4[m-1])
                m=m+1
                
            print("")
            slis4a=sorted(lis4a)
            slis4b=sorted(lis4b)
            tpl4a=tuple(lis4a)
            tpl4b=tuple(lis4b)
            print(f"\nValores altos calculados en formato LISTA: {slis4a}")
            print(f"Valores altos calculados en formato TUPLA: {tpl4a}")
            print(f"\nValores bajos calculados en formato LISTA: {slis4b}")
            print(f"Valores bajos calculados en formato TUPLA: {tpl4b}")
        print("\n¿Desea repetir el programa?")
        print("\n1) Demostración del cálculo de valores altos y bajos. \
              \n2) Salir.")

        op=int(input("\nIngrese una opción: "))    
    if op==2:
        print("\nFIN")

