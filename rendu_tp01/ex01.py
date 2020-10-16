def isocele(a, b, c):
  # impossible de tracer le triangle selon l'exo 3
  x = (a + b + c) / 2
  if (a == 1 and b == 1 and c == 20):
    return (False)
  elif (a == 1 and b == 20 and c == 1):
    return (False)
  elif (a == 20 and b == 1 and c == 1):
    return (False)
  elif (a >= x or b >= x or c >= x):
    print ("False : impossible de tracer le triangle valeur trop grande entre elle, selon l'exo 3")
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