'''
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
location = input("What is your location? ")
age = input("What is your age? ")
space = " "
print("Hi " + firstName + space + lastName + "\n"+"! Your location is " +
      location + " and you are " + age + " years old.")
'''




'''while True:
    x=input("ingrese un valor hasta el cual contar ")
    if x== "q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
        print (y)
        y=y+1
        if y>x:
            break
    '''
    
    
'''
word = input('Introduce una palabr')
for i in range(10):
    print (word)
    
'''
'''
def message ():
    print ('Enter next value')
print ('We start here')
message ()
message ()
message ()


print ('The end is here')
'''
'''
def message ():
    print ('un numerito:')

message ()
a = int (input())
message ()
b = int (input())
message ()
c = int (input())
'''

'''
def HOLA (nombre):
    print ('HOLA, ', nombre)

HOLA ('Fito')
    

def hiAll (name1, name2):
    print ('Hi,', name2)
    print ('Hi,', name1)
    
hiAll ('Sebastian', 'Vega')
'''
    
'''
def hiAll (name1, name2, name3):
    print ('Hi,', name1)
    print ('Hi,', name2)
    print ('Hi,', name3)
    
hiAll ('Sebastian', 'Vega', 'Monsalve')
hiAll ('SEbastian', 'VEga', 'MOnsalve')
'''

'''
#-----------
def direccion (Ciudad, Calle, Codigo Postal):
    print ('Vives en la ciudad de:', Ciudad, ' Tu casa esta ubicada en la calle: ', Calle, 'Tú codigo postal es: ')
C =input('Ciudad:: ')
Cll= input ('Calle:: ')
CP= input ('Codigo Postal:: ')

direccion (C, Cll, CP)
'''

'''
def subtra (a, b):
    print (a - b)

subtra (a=5, b=2)       #outputs:3
subtra (b=2, a=5)       #outputs:3
'''



'''
def resta (a,b):
    print (a-b)

resta (5, b=2)          #primero se asigna solo lo de la derecha 
resta (a=5, 2)          #este dara error ya que se esta poniendo la primera letra de la izquierda
'''


'''
def multiplica (a, b):
    return a*b
print (multiplica (3, 4))


def multiplica (a, b):
    return 
print (multiplica (3, 4))
'''

'''
def wishes():
    return 'Feliz Cumpleaños César Montero....!'
x=wishes()
print (x)
'''

'''
#-------------------------
def wishes ():
    print ('My wishes')
    return 'Feliz Cumple'
wishes ()

def wishes ():
    print ('My wishes)
'''


'''
def Hola (Mylist):
    for name in Mylist:
        print ('Hola, ', name)
    
Hola (['Luis', 'Jonh', 'Jose'])
'''
'''
def createList (n):
    myList =[]
    for i in range (n):
        myList.append (i)
        
    return myList
print (createList(5))
'''

def isPrime(n):
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print (isPrime(12))

#for i in range (29112019, 30122070):
#    if isPrime(i+1):
#        print (i+1, end=' ')

#print()



























    
    
    
    
    
    
    
    
    
    