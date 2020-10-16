
def definit_triangle(a, b, c):
  # verif si positif
  if (a < 0 or b < 0 or c < 0):
    return (False)
  x = (a + b + c) / 2
  if (a >= x or b >= x or c >= x):
    return (False)
  return (True)

def simulation_ex03():
  print (" ")
  print ("definit_triangle(1,1,20) -> ", definit_triangle(1,1,20))
  print ("definit_triangle(4,2,3) -> ", definit_triangle(4,2,3))
  print ("definit_triangle(4,4,4) -> ", definit_triangle(4,4,4))
  print (" ")
