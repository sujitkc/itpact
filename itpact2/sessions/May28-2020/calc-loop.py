while(True):
  choice = int(input("Enter your choice: "))

  x = int(input("Enter the first number: "))
  y = int(input("Enter the second number: "))
  answer = 0
  if(choice == 1):
    print("Adding " + str(x) + " and " + str(y) + " ...")
    answer = x + y
  elif(choice == 2):
    print("Subtracting " + str(x) + " and " + str(y) + " ...")
    answer = x - y
  elif(choice == 3):
    print("Multiplying " + str(x) + " and " + str(y) + " ...")
    answer = x * y
  elif(choice == 4):
    print("Dividing " + str(x) + " and " + str(y) + " ...")
    answer = x / y
  else:
    print("Nothing happened. Quitting ...")
    break

  print(answer)

print("Good bye!!")
