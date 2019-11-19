'''
Tarea 05
@author: cesarmontero
'''



nombre_y_apellido = input ('Cual es tu nombre y apellido: ')
ubicacion = input('Tu recidencia actual es: ')
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
    
print ('Bienvenido a PRO SAK ' + nombre_y_apellido + ubicacion + spacio + 'por tus ' , edad , ' años, hemos preparado esto para ti...!' + 'gracias por visitarnos...!')

