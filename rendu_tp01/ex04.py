

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
  print (" ")
  print ("test : nb_triangles_speciaux(1,20)")
  print ("ensemble des combinaisons")
  print ("result : ", nb_triangles_speciaux(1,20))
  print (" ")