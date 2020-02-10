from math import sqrt

#while (True):                                                  
a = float(input(" \n" + "Введите значение a = "))                                  
b = float(input("Введите значение b = "))
c = float(input("Введите значение c = "))


if a == 0 and b == 0 and c == 0:
    print(" \n" + "бесконечное множество решений")
    #continue




if a == 0 and b == 0 and c != 0:
    print(" \n" + "нет решений")
     #continue
    
if a == 0 and b != 0 and c == 0:
    print(" \n" + "x = 0") 
    #continue
    
if a != 0 and b == 0 and c == 0:
    print(" \n" + "x = 0") 
    #continue
    
if a == 0 and b != 0 and c != 0:
    print(" \n" + "x = " + str( -c/b ))
    #continue
    
if a != 0 and b == 0 and c != 0:
    h = -c/a
    
    if h > 0 :
        
        print(" \n" + "x_1 = " + str( sqrt(h) ))
        print("x_1 = " + "√" + str( h ))
        
        print(" \n" + "x_2 = " + str( -1*sqrt(h) ))
        print("x_2 = " + "-√" + str( h ))
        #continue
    
    else:
        print(" \n" + "x_1 = " + str( sqrt(-h) ) + 'i')
        print("x_1 = √" + str(h))
        print(" \n" + "x_2 = -" + str( sqrt(-h) ) + 'i')
        print("x_2 = -√" + str(h))
        print(" \n" + "где i = √-1")
        #continue        
        

if a != 0 and b != 0 and c == 0:
    print(" \n" + "x_1 = 0")
    print(" \n" + "x_2 = " + str( -b/a ))
    print("x_2 = " + str(-b) + "/" + str(a))
    #continue


'''

D = b**2.0- 4.0*a*c

if D < 0.0:
    print("уравнение не имеет решений диствительних числах")
    
#if D > 0.0:
    
#if a == 0:
#    print("x_1 = " + str(-c/b)
   
    
    
if a > 0:
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)
    print("x_1 = ",x1)
    print("x_2 = ",x2)
        
    
if D == 0.0:
    
    if a == 0:
        print("x = 0")
        
    if a > 0:
        x = -b / (2 * a)
        print("x =",x)
'''
        
