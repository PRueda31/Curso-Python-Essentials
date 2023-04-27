# Código para separar números pares de impares y detectar valores atípicos
# En este código se considera un valor atípico a todo número igual o mayor a 100 
Datos_2021 = [1, 2, 3, 4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]
# Declaración de variables

n=0
m=0
n1=0
n2=0
b=[]
c=[]
d=[]

while n<=len(Datos_2021)-1:
    a=Datos_2021[n]%2
    if Datos_2021[n]>=100:
       d.insert(m,Datos_2021[n]) 
       m=m+1
    if a==0:
        b.insert(n1,Datos_2021[n])
        n1=n1+1
    else:
        c.insert(n2,Datos_2021[n])
        n2=n2+1
    n=n+1
print("\nPares")
print(b)
print("\nImpares")
print(c)
print("\nValores atípicos")
print(sorted(d))
