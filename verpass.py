print("\nPrograma para validar contraseñas")
print("\nPara ingresar su contraseña, considere que ésta debe cumplir con lo siguiente: \
    \n\n-Tener al menos una minúscula entre 'a','b','c','d','e','f','g','h','i','j'. \
    \n-Tener al menos una mayúscula entre 'K','L','M','N','O','P','Q','R','S','T'. \
    \n-Tener al menos un número comprendido entre 0 y 9. \
    \n-Tener al menos uno de los siguientes caracteres: $, %, *, @")

a=list(input("\nIngrese su contraseña: "))

lis1=["a","b","c","d","e","f","g","h","i","j"]
lis2=["K","L","M","N","O","P","Q","R","S","T"]
lis3=["0","1","2","3","4","5","6","7","8","9"]
lis4=["$","%","*","@"]
lisg=lis1+lis2+lis3+lis4

nlis1=len(lis1)
nlis2=len(lis2)
nlis3=len(lis3)
nlis4=len(lis4)
nlisg=len(lisg)

opg=lisg+a

n=0
n1=0
n2=0
n3=0
n4=0

while n<nlisg:
    if opg.count(lis1[n1])>=2:
        if opg.count(lis2[n2])>=2:
            if opg.count(lis3[n3])>=2:
                if opg.count(lis4[n4])>=2:
                    if len(a)>=5 and len(a)<=15:
                        print("\nLa contraseña cumple con todas las especificaciones.")
                        break
                    else:
                        print("\nLa contraseña debe tener entre 5 y 15 caracteres.")
                        break
                else:
                    n4=n4+1
                if n4==nlis4-1 and opg.count(lis4[n4])<2:
                    print("\nLa contraseña debe tener al menos uno de los siguientes caracteres: $, %, *, @")
                    break
            else:
                n3=n3+1
            if n3==nlis3-1 and opg.count(lis3[n3])<2:
                print("\nLa contraseña debe tener al menos un número comprendido entre 0 y 9.")
                break
        else:
            n2=n2+1
        if n2==nlis2-1 and opg.count(lis2[n2])<2:
            print("\nLa contraseña debe tener al menos una mayúscula comprendida entre \
                  'K','L','M','N','O','P','Q','R','S','T'.")
            break
    else:
        n1=n1+1
    if n1==nlis1-1 and opg.count(lis1[n1])<2:
        print("\nLa contraseña debe tener al menos una minúscula comprendida entre \
              'a','b','c','d','e','f','g','h','i','j'.")
        break
    
