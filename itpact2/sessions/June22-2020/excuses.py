'''
Make an excuse for not turning up for ITPACT class by
combining any one of the phrases in each column.


  MY MOTHER     |    TORE UP     |   MY HOMEWORK    
  MY DOG        |    ATE         |   MY BUS 
  MY PINKY TOE  |    STEPPED ON  |   MY BEDROOM    
  A RANDOM GUY  |    INJURED     |   MY CLOTHES            
  THE TOILET    |    SMACKED     |   MY LUNCH          
  A COCROACH    |    SMOOSHED    |   YOUR MONEY        

'''

word1 = [
  "MY MOTHER",
  "MY DOG",
  "MY PINKY TOE",
  "A RANDOM GUY",
  "THE TOILET",
  "A COCROACH"
]

word2 = [
  "TORE UP",
  "ATE",
  "STEPPED ON",
  "INJURED",
  "SMACKED",
  "SMOOSHED"
]

word3 = [
  "MY HOMEWORK",
  "MY BUS",
  "MY BEDROOM",
  "MY CLOTHES",
  "MY LUNCH",
  "YOUR MONEY"
]

# nested loops
for w1 in word1:
  for w2 in word2:
    for w3 in word3:
      print(w1 + " " + w2 + " " + w3 + "!")
