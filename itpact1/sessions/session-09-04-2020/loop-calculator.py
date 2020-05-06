import sys

# I want to modify the program as follows:
# The program should not quit after doing a calculation.
# Instead it should ask for the choice again.
# If choice is 5 then it should quit.
# Else it should do the calculation and ask for choice again.
# Repeatedly.

# input function returns a 'string'.
# We want an integer as a choice.
# We convert the string into an integer.
while(True):
  choice = int(input("Enter your choice" +
                   " (1 for addition," +
                   " 1 for multiplication ," +
                   " 3 for division, " +
                   " 4 for substraction), " +
                   " 5 to quit : "))

  if(choice==5):
    print("Quitting ...")
    sys.exit(0) # command for exiting the program.
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))
  if(choice == 1):
    print (a + b)
  elif(choice == 2):
    print(a * b)
  elif(choice==3):
    print (a/b)
  elif(choice==4):
    print (a-b)
  else:
    print("Invalid choice")
