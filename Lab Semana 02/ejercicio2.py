from random import randint     
#Inicio

lista=[]

for i in range(3):
    lista.append(int(input("Introduce un número (N,M,S): ")))

print(lista)

#M lineas (p,t) 

p=[]
t=[]
for i in range(lista[1]):
   p.append(randint(1,lista[0])) #ID socio
   t.append(randint(1,10000)) #ID del terminal
print(p,t)

#S lineas (c,t)
c=[]
t=[]

for i in range(lista[2]):
    c.append(randint(1,10000)) #ID del cliente
             


        





