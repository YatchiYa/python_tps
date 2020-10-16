

import math
from ex01 import *
from ex02 import *
from ex04 import *
from ex03 import *

print ("TP1 simulation : ")
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