def lis(s): 
    """RETURNS LIST ELEMENTS TO STRING"""
    str1 = "" 
    for ele in s:                     
        str1 += ele   
    return str1 


def randomLetters(amount:int):
    """ARRAY GENERATION OF RANDOM ALPHABETS"""
    return random.choices(string.ascii_uppercase, k=amount)    
i=0
j=0                                  
#d =  np.array(randomLetters(i*j)).reshape((i,j))


#Reversal of array
def rev(x):
  """RETURNS REVERSED ARRAY"""
  new = []                        
  for i in x[::-1]:
    new.append(i)
    x = new
  return x                           