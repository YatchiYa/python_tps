
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
  print (" ")
  print ("air_ordonne(4,2,3) -> ", air_ordonne(4,2,3))
  print ("air_ordonne(4,3,3) -> ", air_ordonne(4,3,3))
  print ("air_ordonne(4,4,4) -> ", air_ordonne(4,4,4))
  print ("air_ordonne(3,4,5) -> ", air_ordonne(3,4,5))
  print ("air_ordonne(13,14,15) -> ", air_ordonne(13,14,15))
  print ("air_ordonne(1,1,1) -> " , air_ordonne(1,1,1))
  print (" ")