
# **************************************************************************************************************
#                                       Rendu du TP 02
#                                         Youcef ARAB
#                                         Master 1 BD
# 
# **************************************************************************************************************



# ---------------------------------------------------------------------------------------------------------------
#                                        EXO1
# ---------------------------------------------------------------------------------------------------------------

def skip_space(word, i):
    while (i < len(word) and word[i] == ' '):
        i += 1
    return (i)

def quote_found(word, i, ret, quote):
    if (i == ' '):
        while (i < len(word) and word[i] == ' '):
            i += 1
    while (i < len(word) and word[i] != quote):
        if (word[i] == ' '):
            i = skip_space(word, i)
        else:
            while (i < len(word) and word[i] != ' '):
                i += 1
            ret += 1
    i += 1
    return (i, ret)

def compte_mots(word):
    ret = 0
    i = 0
    while (i < len(word)):
        if (word[i] == ' '):
            i += 1
        elif (word[i] == '"'):
            i += 1
            i, ret = quote_found(word, i, ret, '"')
        elif (word[i] == '\''):
            i += 1
            i, ret = quote_found(word, i, ret, '\'')
        else:
            while (i < len(word) and word[i] != ' '):
                i += 1
            ret += 1
    return (ret)

def simulation_exo1():
    print ("------------------------ EXO 1 ------------------------------")
    print ("\" --> ", compte_mots("\""))
    print("\"il ingurgite impunment un iguane.\" --> ", compte_mots("\"il ingurgite impunment un iguane.\""))
    print ("\"coursdeprogrammation\" --> ", compte_mots("\"coursdeprogrammation\""))
    print ("Helloooooooooo  yeahhhh world is like hell --> ", compte_mots("Helloooooooooo  yeahhhh world is like hell"))
    print ("\" Attention aux espaces consecutifs ou terminaux \" --> ", compte_mots("\" Attention aux espaces consécutifs ou terminaux \""))
                
simulation_exo1()




# ---------------------------------------------------------------------------------------------------------------
#                                        EX02
# ---------------------------------------------------------------------------------------------------------------

def remplace_multiple(src, replace, n):
    i = 0
    j = 0
    if (n < 0):
        print ("error : taille negative ")
        return 
    if (len(src) == 0 or len(replace) == 0):
        print ("error : taille de la source our replace est null ")
        return 
    dest = str()
    while (i < len(src) and i < n):
        dest += src[i]
        i += 1
    if (i == n):
        while (i < len(src) and j < len(replace)):
            if (i == (j + 1)*n):
                dest += replace[j]
                j += 1
                i += 1
            else:
                dest += src[i]
                i += 1
        while (i < len(src)):
            dest += src[i]
            i += 1
        while (j < len(replace)):
            dest += replace[j]
            j += 1
    return (dest)

def simulation_exo2():
    print ("------------------------ EXO 2 ------------------------------")
    print ('remplace_multiple("\"","\"",2) --- ', remplace_multiple("\"","\"",2))
    print ('remplace_multiple("abacus", "oiseau",2) --- ', remplace_multiple("abacus", "oiseau",2))
    print ('remplace_multiple("hirondelles","nid",3) --- ', remplace_multiple("hirondelles","nid",3))
    print ('remplace_multiple("Hello","World",4) --- ', remplace_multiple("Hello","World",4))
    print ('remplace_multiple("Life is like *****","hell", 1) --- ', remplace_multiple("Life is like *****","hell", 1))
    print ('remplace_multiple("Life is like *****","hell", -51) --- ', remplace_multiple("Life is like *****","hell", -51))
    print ('remplace_multiple("Hello from the other side","this is", 5) --- ', remplace_multiple("Hello from the other side","this is", 5))


simulation_exo2()


# ---------------------------------------------------------------------------------------------------------------
#                                        EX03 : p1
# ---------------------------------------------------------------------------------------------------------------

def calcule_u_index(n, u):
    if (n == 0):
        return (1)
    elif (n == 1):
        return (u * pow(2, n) + n)
    else:
        return (calcule_u_index(n - 1, u) * pow(2, n) + n)

def termeU(index):
    u0 = 1
    return (calcule_u_index(index, u0))
        

def simulation_exo3():
    print ("------------------------ EXO 3 -P1- ------------------------------")
    print ("termeU(0) -- ", termeU(0))
    print ("termeU(1) -- ", termeU(1))
    print ("termeU(5) -- ", termeU(5))
    print ("termeU(10) -- ", termeU(10))
    print ("termeU(50) -- ", termeU(12))


simulation_exo3()


# ---------------------------------------------------------------------------------------------------------------
#                                        EX03 : p2
# ---------------------------------------------------------------------------------------------------------------

"""
# redefinition de la fontion juste dans le cas ou on execute l'exo 3 partie 2 séparé de l'exo3 partie 1
def calcule_u_index(n, u):
    if (n == 0):
        return (1)
    elif (n == 1):
        return (u * pow(2, n) + n)
    else:
        return (calcule_u_index(n - 1, u) * pow(2, n) + n)

def termeU(index):
    u0 = 1
    return (calcule_u_index(index, u0))
"""

def serie(index):
    i = 0
    somme = 0
    if (index < 0):
        print ("error : index negative")
        return
    while (i <= index):
        somme =  somme + termeU(i)
        i += 1
    return (somme)
        

def simulation_exo4():
    print ("------------------------ EXO 3 -P2- ------------------------------")
    print ("serie(0) -- ", serie(0))
    print ("serie(1) -- ", serie(1))
    print ("serie(5) -- ", serie(5))
    print ("serie(10) -- ", serie(10))
    print ("serie(50) -- ", serie(50))


simulation_exo4()


# ---------------------------------------------------------------------------------------------------------------
#                                        EX03 : p2
# ---------------------------------------------------------------------------------------------------------------


def serie_v2(index):
    i = 1
    u0 = 1
    u_index = u0
    somme = u_index
    if (index < 0):
        print ("error : index negative")
        return
    if (index == 0):
        return (1)
    while (i <= index):
        u_index = (u_index * pow(2, i)) + i
        somme =  somme + u_index
        i += 1
    return (somme)

    
def simulation_exo5():
    print ("------------------------ EXO 3 -P2- ------------------------------")
    print ("serie_v2(0) -- ", serie_v2(0))
    print ("serie_v2(1) -- ", serie_v2(1))
    print ("serie_v2(5) -- ", serie_v2(5))
    print ("serie_v2(10) -- ", serie_v2(10))
    print ("serie_v2(50) -- ", serie_v2(50))

simulation_exo5()



# ---------------------------------------------------------------------------------------------------------------
#                                        EX03 : p3
# ---------------------------------------------------------------------------------------------------------------


def show(index):
    i = 1
    j = -1
    u0 = 1
    u_index = u0
    somme = u_index
    if (index < 0):
        print ("error : index negative")
        return
    if (index == 0):
        while (j <= index):
            print ("-----------", end=' ')
            j += 1
        j = -1
        print()
        while (j <= index):
            if (j == -1):
                print ("|Iteration|", end=' ')
            else:
                print ("|    u",j,"   |", end=' ')
            j += 1
        j = -1
        print()
        while (j <= index):
            if (j == -1):
                print ("|   ",j+1,"   |", end=' ')
            else:
                print ("|   ",u_index,"     |", end=' ')
            j += 1
        j = -1
        print()
        while (j <= index):
            print ("-----------", end=' ')
            j += 1
        return (1)
    return (somme)

    
def simulation_exo6():
    print ("------------------------ EXO 3 -P3- ------------------------------")
    show(0)

#simulation_exo6()



# ---------------------------------------------------------------------------------------------------------------
#                                        EX03 - p4 -
# ---------------------------------------------------------------------------------------------------------------

import time

def time_test():
    print ("------------------------ EXO 3 -P4- ------------------------------")
    depart = time.time()
    serie_v2(500)
    arrive = time.time()
    ret = arrive-depart
    print ("temps en sec de serie_v2(500) : ", ret)
    depart = time.time()
    serie(500)
    arrive = time.time()
    ret2 = arrive-depart
    print ("temps en sec de serie(500) :    ", ret2)



    depart = time.time()
    serie_v2(250)
    arrive = time.time()
    ret = arrive-depart
    print ("temps en sec de serie_v2(250) : ", ret)
    depart = time.time()
    serie(250)
    arrive = time.time()
    ret2 = arrive-depart
    print ("temps en sec de serie(250) :    ", ret2)

    
    depart = time.time()
    serie_v2(100)
    arrive = time.time()
    ret = arrive-depart
    print ("temps en sec de serie_v2(100) : ", ret)
    depart = time.time()
    serie(100)
    arrive = time.time()
    ret2 = arrive-depart
    print ("temps en sec de serie(100) :    ", ret2)

    if (ret2 > ret):
        print ("serie_v2 est bien plus performante que serie")
    else:
        print ("serie est bien plus performante que serie_v2")
    print ("et c'est verifie l'algo de serie_v2 est bien plus performant que celui implemente sur series")

time_test()



# ---------------------------------------------------------------------------------------------------------------
#                                        EX04
# ---------------------------------------------------------------------------------------------------------------

def factorielle(n):
    if (n < 0):
        return ("error : impossible de calcule le fact d'un nombre négatif")
    elif (n == 0):
        return (1)
    else:
        return (factorielle(n - 1) * n)

def simulation_exo7():
    print ("------------------------ EXO 4 ------------------------------")
    print("fac(2) -- ", factorielle(1))
    print("fac(2) -- ", factorielle(2))
    print("fac(2) -- ", factorielle(3))
    print("fac(2) -- ", factorielle(4))
    print("fac(5) -- ", factorielle(5))
    print("fac(10) -- ", factorielle(10))
    print("fac(7) -- ", factorielle(7))
    print("fac(0) -- ", factorielle(0))
    print("fac(-5) -- ", factorielle(-5))

simulation_exo7()


# ---------------------------------------------------------------------------------------------------------------
#                                        main_test
# ---------------------------------------------------------------------------------------------------------------

#import math
#from ex01 import *
#from ex02 import *
#from ex04 import *
#from ex03 import *

print ("-------------------------------------------------------------------- ")
print ("vous desirez revoir exo par exo du TP2 ? ")
x = input("please enter your exercice number : [1,2,3,4] or 0 to quit : ")

while (x != 0):
  if (x == '4'):
    simulation_exo7()
  elif (x == '1'):
    simulation_exo1()
  elif (x == '2'):
    simulation_exo2()
  elif (x == '3'):
    simulation_exo4()
    simulation_exo5()
    simulation_exo6()
    time_test()
  elif (x == '0'):
    break
  else:
    print ("commande not exist")
  x = input("please enter your exercice number : [1,2,3,4] or 0 to quit : ")

print ("ciao ! ")