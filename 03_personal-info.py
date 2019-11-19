'''
nombre_y_apellido = input ('Cual es tu nombre y apellido: ')
ubicacion = input(' Tu recidencia actual es: ')
edad = int(input('tu edad es: '))
spacio = ' '

if edad < 18:
    print ('Eres menor de edad, intentalo a los 18')
elif edad>19 and edad<=70:
    print  ('Esperamos ser de tu agrado')
elif edad>71 and edad<100:
    print  ('Tenemos grandes descuentos en medicina')
else:
    print ('Te hemos registrado, te visitaremos pronto')
    
print ('Bienvenido a PRO SAK: ' + nombre_y_apellido + ' ,estas ubicado en la ciudad de: '+ ubicacion + spacio + '/adios...!')
'''


'''
devices = ['R1', 'R2', 'R3', 'S1', 'S2']
for item in [devices]:
    print (item)
'''
'''    
#a=['comienzo', 'final']
print ('comienzo')
for i in [4]:
    print ('Hola', end ='')
print ()
print ('Final')  

'''

'''
devices = ['R1', 'R2', 'R3', 'S1', 'S2']
for item in [devices]:
    if 'R' in item:
        print (item)
'''











