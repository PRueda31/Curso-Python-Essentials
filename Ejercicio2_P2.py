print("\nPrograma para validar contrase�as")
print("\nPara ingresar su contrase�a, considere que �sta debe cumplir con lo siguiente: \
    \n\n-Tener al menos una min�scula entre 'a','b','c','d','e','f','g','h','i','j'. \
    \n-Tener al menos una may�scula entre 'K','L','M','N','O','P','Q','R','S','T'. \
    \n-Tener al menos un n�mero comprendido entre 0 y 9. \
    \n-Tener al menos uno de los siguientes caracteres: $, %, *, @")

a=list(input("\nIngrese su contrase�a: "))

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
                        print("\nLa contrase�a cumple con todas las especificaciones.")
                        break
                    else:
                        print("\nLa contrase�a debe tener entre 5 y 15 caracteres.")
                        break
                else:
                    n4=n4+1
                if n4==nlis4-1 and opg.count(lis4[n4])<2:
                    print("\nLa contrase�a debe tener al menos uno de los siguientes caracteres: $, %, *, @")
                    break
            else:
                n3=n3+1
            if n3==nlis3-1 and opg.count(lis3[n3])<2:
                print("\nLa contrase�a debe tener al menos un n�mero comprendido entre 0 y 9.")
                break
        else:
            n2=n2+1
        if n2==nlis2-1 and opg.count(lis2[n2])<2:
            print("\nLa contrase�a debe tener al menos una may�scula comprendida entre \
                  'K','L','M','N','O','P','Q','R','S','T'.")
            break
    else:
        n1=n1+1
    if n1==nlis1-1 and opg.count(lis1[n1])<2:
        print("\nLa contrase�a debe tener al menos una min�scula comprendida entre \
              'a','b','c','d','e','f','g','h','i','j'.")
        break
