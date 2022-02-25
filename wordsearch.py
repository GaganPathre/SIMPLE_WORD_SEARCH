import numpy as np
import string
import random
ai=[]
l = []

################################FUNCTION LINE###################################

def lis(s): 
    str1 = "" 
    for ele in s:                     #CONVERTING LIST ELEMENTS TO STRING
        str1 += ele   
    return str1 


def randomLetters(amount:int):
    return random.choices(string.ascii_uppercase, k=amount)    

i=0
j=0                                  #ARRAY GENERATION OF RANDOM ALPHABETS

d =  np.array(randomLetters(i*j)).reshape((i,j))

################################################################################

#WORDS IN THE ARRRAY: salt, heat, song, jay, ola, nathan, iris, lukas

#LOGIC AREA

puzz =np.array(['I', 'L', 'W', 'R', 'Z', 'E', 'J', 'A', 'Y', 'J',
                'M', 'B', 'G', 'T', 'L', 'D', 'J', 'C', 'P', 'E',
                'L', 'U', 'K', 'A', 'S', 'J', 'T', 'B', 'M', 'D',
                'K', 'B', 'G', 'O', 'L', 'U', 'K', 'E', 'I', 'C',
                'N', 'A', 'T', 'H', 'A', 'N', 'H', 'O', 'F', 'G',
                'S', 'O', 'N', 'G', 'A', 'R', 'H', 'L', 'A', 'T',
                'I', 'R', 'I', 'S', 'B', 'R', 'S', 'A', 'L', 'T',
                'Y', 'D', 'N', 'C', 'Y', 'A', 'T', 'L', 'W', 'A',
                'W', 'I', 'A', 'U', 'X', 'I', 'X', 'L', 'V', 'S',
                'O', 'U', 'P', 'N', 'P', 'X', 'U', 'X', 'N', 'R']).reshape(10,10)

print(puzz)


#Accepting the number of words and storing them in a list.

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

#Traversing through the list word by word while searching the word using nested loop  

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
