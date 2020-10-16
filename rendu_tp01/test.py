


# **************************************************************************************************************
#                                       Rendu du TP 01
#                                         Youcef ARAB
#                                         Master 1 BD
# 
# **************************************************************************************************************



# ---------------------------------------------------------------------------------------------------------------
#                                        EXO1
# ---------------------------------------------------------------------------------------------------------------
def isocele(a, b, c):
  # declaration de variable pour l'impossiblité de tracer le triangle selon l'exo 3
  x = (a + b + c) / 2
  if (a == 1 and b == 1 and c == 20):
    return (False)
  elif (a == 1 and b == 20 and c == 1):
    return (False)
  elif (a == 20 and b == 1 and c == 1):
    return (False)
  elif (a >= x or b >= x or c >= x):
    print ("False : impossible de tracer le triangle car les valeurs sont trop grandes entre elles, selon l'exo 3")
    return (False)
  elif (a == b or a == c):
    return (True)
  elif (b == a or b == c):
    return (True)
  elif (c == a or c == b):
    return (True)
  else :
    return (False)

def simulation_ex01():
  print (" -------------------------- Ex01 ---------------------------------")
  print (" ")
  print ("isocele(4,2,3) -> ", isocele(4,2,3)) 
  print ("isocele(4,5,7) -> ", isocele(4,5,7))
  print ("isocele(4,3,3) -> ", isocele(4,3,3))
  print ("isocele(4,4,4) -> ", isocele(4,4,4))
  print ("isocele(5,4,4) -> ", isocele(5,4,4))
  print (" cas special :")
  print ("isocele(1,1,20) -> ", isocele(1,1,20))
  print ("isocele(1,20,1) -> ", isocele(1,20,1))
  print ("isocele(20,1,1) -> ", isocele(20,1,1))
  print (" ")

simulation_ex01()


# ---------------------------------------------------------------------------------------------------------------
#                                        EXO2
# ---------------------------------------------------------------------------------------------------------------

import math 

def air_ordonne(a, b, c):
  # select min and max value for u1 u2 u3
  # u1 : min value
  # u3 : max value
  # u2 : mid value
  # start verif
  u3 = max(a,b,c)
  if (u3 == a):
    u1 = min(b,c)
    if (u1 == b):
      u2 = c
    else:
      u2 = b
  elif (u3 == b):
    u1 = min(a,c)
    if (u1 == a):
      u2 = c
    else:
      u2 = c
  elif (u3 == c):
    u1 = min(a,b)
    if (u1 == a):
      u2 = b
    else:
      u2 = a
  # end of verif
  x = math.pow(u1,2) * math.pow(u3,2)
  y = (math.pow(u1,2) - math.pow(u2,2) + math.pow(u3,2)) / 2
  z = x - math.pow(y,2)
  final = (math.sqrt(z)) / 2
  return (final)


def simulation_ex02():
  print (" -------------------------- Ex02 ---------------------------------")
  print (" ")
  print ("air_ordonne(4,2,3) -> ", air_ordonne(4,2,3))
  print ("air_ordonne(4,3,3) -> ", air_ordonne(4,3,3))
  print ("air_ordonne(4,4,4) -> ", air_ordonne(4,4,4))
  print ("air_ordonne(3,4,5) -> ", air_ordonne(3,4,5))
  print ("air_ordonne(13,14,15) -> ", air_ordonne(13,14,15))
  print ("air_ordonne(1,1,1) -> " , air_ordonne(1,1,1))
  print (" ")

simulation_ex02()


# ---------------------------------------------------------------------------------------------------------------
#                                      EXO3
# ---------------------------------------------------------------------------------------------------------------


def definit_triangle(a, b, c):
  # verif si positif
  if (a < 0 or b < 0 or c < 0):
    return (False)
  x = (a + b + c) / 2
  if (a >= x or b >= x or c >= x):
    return (False)
  return (True)

def simulation_ex03():
  print (" -------------------------- Ex03 ---------------------------------")
  print (" ")
  print ("definit_triangle(1,1,20) -> ", definit_triangle(1,1,20))
  print ("definit_triangle(4,2,3) -> ", definit_triangle(4,2,3))
  print ("definit_triangle(4,4,4) -> ", definit_triangle(4,4,4))
  print ("definit_triangle(2,6,2) -> ", definit_triangle(2,6,2))
  print ("definit_triangle(2,5,2) -> ", definit_triangle(2,5,2))
  print ("definit_triangle(2,4,2) -> ", definit_triangle(2,4,2))
  print ("definit_triangle(2,4,3) -> ", definit_triangle(2,4,3))
  print ("definit_triangle(1,1,1) -> ", definit_triangle(1,1,1))
  print (" ")


simulation_ex03()



# ---------------------------------------------------------------------------------------------------------------
#                                        EXO4
# ---------------------------------------------------------------------------------------------------------------



import math

# def of perimetre function
def perim(a, b, c):
  return (a + b +c)

# def of valid triangle
def definit_triangle(a, b, c):
  # verif si positif
  if (a < 0 or b < 0 or c < 0):
    return (False)
  x = (a + b + c) / 2
  if (a >= x or b >= x or c >= x):
    return (False)
  return (True)


# def air of triangle
def air_ordonne(a, b, c):
  # select min and max value for u1 u2 u3
  # u1 : min value
  # u3 : max value
  # u2 : mid value
  # start verif
  u3 = max(a,b,c)
  if (u3 == a):
    u1 = min(b,c)
    if (u1 == b):
      u2 = c
    else:
      u2 = b
  elif (u3 == b):
    u1 = min(a,c)
    if (u1 == a):
      u2 = c
    else:
      u2 = c
  elif (u3 == c):
    u1 = min(a,b)
    if (u1 == a):
      u2 = b
    else:
      u2 = a
  # end of verif
  x = math.pow(u1,2) * math.pow(u3,2)
  y = (math.pow(u1,2) - math.pow(u2,2) + math.pow(u3,2)) / 2
  z = x - math.pow(y,2)
  # sqrt d'un nombre negative est impossible 
  # return -1 just for showinf it's an error (false in my if)
  if (z < 0):
    return (-1)
  final = (math.sqrt(z)) / 2
  return (final)

# to check for duplicates : our a must be below our b and same goes for c because it's already verified in while loop 
def check_duplicat(i, j, k):
  if (i <= j and j <= k):
    return (True)
  return (False)

# function 
def nb_triangles_speciaux(n,p):
  if (n < 0 or p < 0):
    return ("error :> nombre n or p negative")
  if (n > p):
    return ("error :> please specify n > p when you call the function (n,p)")
  i = n
  ret = 0
  while (i <= p):
    j = n
    while (j <= p):
      k = n
      while (k <= p):
        if (definit_triangle(i, j, k)):
          if (air_ordonne(i, j, k) == perim(i, j, k)):
            if (check_duplicat(i, j, k)):
              print ("(", i, ",", j, ",", k, ")")
              ret += 1
        k += 1
      j += 1
    i += 1
  
  return (ret)


def simulation_ex04():
  print (" -------------------------- Ex04 ---------------------------------")
  print (" ")
  print ("test : nb_triangles_speciaux(1,20)")
  print ("ensemble des combinaisons")
  print ("result : ", nb_triangles_speciaux(1,20))
  print (" ")
  print (" ")
  print ("test : nb_triangles_speciaux(1,50)")
  print ("ensemble des combinaisons")
  print ("result : ", nb_triangles_speciaux(1,50))
  print (" ")
  print (" ")
  print ("test : nb_triangles_speciaux(8,20)")
  print ("ensemble des combinaisons")
  print ("result : ", nb_triangles_speciaux(8,20))
  print (" ")
  print (" ")
  print ("test : nb_triangles_speciaux(8,50)")
  print ("ensemble des combinaisons")
  print ("result : ", nb_triangles_speciaux(8,50))
  print (" ")
  print (" ")
  print ("test : nb_triangles_speciaux(-5,-6)")
  print ("ensemble des combinaisons")
  print ("result : ", nb_triangles_speciaux(-9,-6))
  print (" ")
  print (" ")
  print ("test : nb_triangles_speciaux(-5,60)")
  print ("ensemble des combinaisons")
  print ("result : ", nb_triangles_speciaux(-9,60))
  print (" ")


simulation_ex04()




# ---------------------------------------------------------------------------------------------------------------
#                                        main_test
# ---------------------------------------------------------------------------------------------------------------

#import math
#from ex01 import *
#from ex02 import *
#from ex04 import *
#from ex03 import *

print ("-------------------------------------------------------------------- ")
print ("vous desirez revoir exo par exo du TP1 ? ")
x = input("please enter your exercice number : [1,2,3,4] or 0 to quit : ")

while (x != 0):
  if (x == '4'):
    simulation_ex04()
  elif (x == '1'):
    simulation_ex01()
  elif (x == '2'):
    simulation_ex02()
  elif (x == '3'):
    simulation_ex03()
  elif (x == '0'):
    break
  else:
    print ("commande not exist")
  x = input("please enter your exercice number : [1,2,3,4] or 0 to quit : ")

print ("ciao ! ")