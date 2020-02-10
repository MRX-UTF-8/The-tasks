#                               Алгоритм программы:
#
#                                Запуск программы       ←       ←       ←       ←       ←       ←       ←
#                                       ↓                                                               ↑
#                           Получить числа от пользователя                                              ↑
#                                       ↓                                                               ↑
#         Рассмотреть все случаи когда какого-то слагаемого не хватает                                  ↑
#                                       ↓                                                               ↑     
#        Оно полное квадратное уравнение (ax^2 + bx + c = 0 где a,b,c != 0 )    →  нет  →  Показать ответ пользователю 
#                                       ↓                                                               ↑
#                                       да                                                              ↑
#                                       ↓                                                               ↑
#              Решить полное квадратное уравнение через дискриминант       →      →     →  Показать ответ пользователю 
#
#

# проблеми : НСК

###############################################################################
# Объявить все функции 
###############################################################################

# Наибольший общий делитель (НОД) 
def НОД(a,b): 
    a = abs(a)
    b = abs(b)
    if float(a) != int(a) or float(b) != int(b):
        return 1
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    
    НОД = a + b
    return НОД


###############################################################################
# Подготовка данных 
###############################################################################

# Что бы подсчитать квадратный корень из числа 
from math import sqrt

# Цикл для того-что-бы не запускать всё время программу 
#while (True):


try:
    
    # ax^2 + bx + c = 0    Наше квадратное уравнениe где a,b,c  какие-то числа                        
    a = float(input(" \n" + "Введите число a = "))                                  
    b = float(input("Введите число b = "))
    c = float(input("Введите число c = "))
    
except ValueError:
    print('')
    print("###############################################################################"+" \n")
    print("Вы ввели не число" + " \n")
    print("###############################################################################"+" \n")
    #continue


###############################################################################
# Проверить данные на все случаи 
###############################################################################

if a == 0 and b == 0 and c == 0:
    
    # При любом х уравнение будет правильное  
    print(" \n" + "бесконечное множество решений")
    # Для того что бы программа остановилась  
    #continue


if a == 0 and b == 0 and c != 0:
    # При любом х уравнение будет не правильное  
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
    print("x = " + str(-c/НОД(c,b)) + "/" + str(b/НОД(c,b)))
    #continue
  
    
# Квадрат даёт два корня положительный и отрицательный 
if a != 0 and b == 0 and c != 0:
    h = -c/a
    НОД(a,b)
    if h > 0 :
        
        print(" \n" + "x_1 = " + str( sqrt(h) ))
        print("x_1 = " + "√(-" + str( c/НОД(c,a) ) + " / " + str( a/НОД(c,a) ) + ")" )
        
        print(" \n" + "x_2 = -" + str( sqrt(h) ))
        print("x_2 = " + "-√(-" + str( c/НОД(c,a) ) + " / " + str( a/НОД(c,a) ) + ")"  )
        #continue
    
    else:
        print(" \n" + "x_1 = " + str( sqrt(-h) ) + 'i')
        print("x_1 = " + "√(" + str( c/НОД(c,a) ) + " / " + str( a/НОД(c,a) ) + ")"  )
        print(" \n" + "x_2 = -" + str( sqrt(-h) ) + 'i')
        print("x_2 = " + "-√(" + str( c/НОД(c,a) ) + " / " + str( a/НОД(c,a) ) + ")"  )
        print(" \n" + "где i = √-1")
        #continue        
        

if a != 0 and b != 0 and c == 0:
    print(" \n" + "x_1 = 0")
    print(" \n" + "x_2 = " + str( -b/a ))
    # придумать ёще НСК
    print("x_2 = " + str(-b) + "/" + str(a))
    #continue

###############################################################################
# Полное квадратное уравнение 
###############################################################################   

else:
    # Подсчёт дискриминанта 
    D = b**2 - 4*a*c
    
    # Если  дискриминанта положительный то даст два действительных числа (вещественные)
    if D > 0.0:
        
        print(" \n" + "x_1 = " + str( (-b + sqrt(D)) / (2*a) ))
        print("x_1= (" + str(-b/НОД(b,2*a) ) + " / " + str( (2*a)/НОД(b,2*a )) + " + √" + str( D/НОД(D,2*a ) ) +") / " + str( (2*a)/НОД(D,2*a ) ) )
        
        print(" \n" + "x_1 = " + str( (-b - sqrt(D)) / (2*a) ))
        print("x_1= (" + str(-b) + " - √" + str(D) +") / " + str( 2*a ) )
        #continue

    # Если  дискриминанта 0 то даст одно число 
    if D == 0.0:
        print(" \n" + "x = " + str( -b/(2*a) ))
        print("x = " + str(-b) + "/" + str( 2*a ) )
        #continue

    # Если  дискриминанта отрицательный  то даст два мнимых  числа 
    else:
        
        print(" \n" + "x_1 = " + str( -b / (2*a) ) + " + " + str( sqrt(-D) / (2*a) ) + "i")
        print("x_1= (" + str(-b) + " + √" + str(D) +") / " + str( 2*a ) )
        
        print(" \n" + "x_2 = " + str( -b / (2*a) ) + " - " + str( sqrt(-D) / (2*a) ) + "i")
        print("x_2 = (" + str(-b) + " - √" + str(D) +") / " + str( 2*a ) )
        print(" \n" + "где i = √-1")
        #continue

###############################################################################
        
        
        
        
        
        
            
            
            
            
            
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            