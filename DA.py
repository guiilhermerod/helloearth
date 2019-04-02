x= int(input('Em qual ano você deseja descobrir a data da Páscoa?:'))

a= x%19
b= x%4
c= x%7
d= (19*a+24)%30
e= (2*b+4*c+6*d+5)%7

#condiçoes
if d+e>9:
    dia= d+e-9
    mes= 4
if d+e<=9:
    dia= d+e+22
    mes= 3

print ('Páscoa:',dia,"/",mes,)
    


