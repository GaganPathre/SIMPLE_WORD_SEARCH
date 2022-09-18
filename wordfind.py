import numpy as np
import string
import random
from search.funx import *
ai=[]
l = []

#WORDS: salt, heat, song, nathan, iris, lukas, susi, olaf
puzz =np.array(['I', 'L', 'W', 'R', 'Z', 'E', 'J', 'A', 'Y', 'J',
                'M', 'B', 'G', 'T', 'L', 'D', 'J', 'C', 'P', 'E',
                'L', 'U', 'K', 'A', 'S', 'I', 'G', 'B', 'M', 'D',
                'K', 'B', 'G', 'O', 'L', 'A', 'A', 'E', 'I', 'C',
                'N', 'A', 'T', 'H', 'A', 'N', 'G', 'O', 'F', 'G',
                'S', 'O', 'N', 'G', 'F', 'R', 'A', 'L', 'A', 'T',
                'I', 'R', 'I', 'S', 'B', 'R', 'N', 'Z', 'N', 'K',
                'Y', 'D', 'N', 'C', 'Y', 'A', 'S', 'A', 'L', 'T',
                'W', 'I', 'A', 'U', 'X', 'I', 'X', 'L', 'V', 'S',
                'O', 'U', 'P', 'N', 'P', 'X', 'U', 'X', 'N', 'R']).reshape(10,10)

print(puzz)


#Accepting the number of words and adding them to a list.
w = int(input("Enter Number of Words: "))
for o in range(w):
  if o == 0:
    l.append(input(f"Enter {o+1}st Word: ").upper())
  elif o == 1:
    l.append(input(f"Enter {o+1}nd Word: ").upper())
  elif o == 2:
    l.append(input(f"Enter {o+1}rd Word: ").upper())
  else:
    l.append(input(f"Enter {o+1}th Word: ").upper())
  
print("---------------------------------------------------")


#Search Algorithm in action.
 
for q in range(len(l)):
  z = len(l[q])
  for k in range(10):
    for i in range(10):
      ai.append(puzz.T[i][k])
    for j in range(10):
      if lis(ai[j:z]) == l[q]:
        print(l[q], "FOUND IN ROW NO.", k+1)
        break
      z+=1
    z = len(l[q])
    ai.clear()
  else:
    for k in range(10):
      for i in range(10):
        ai.append(puzz[i][k])
      for j in range(10):
        if lis(ai[j:z]) == l[q]:
          print(l[q], "FOUND IN COLUMN NO.", k+1)
          break
        z+=1
      z = len(l[q])
      ai.clear()

#GAGANPATHRE
