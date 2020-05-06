a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
choice = int(input("Enter your choice (1 for addition, 2 for multiplication) : "))
if(choice == 1):
  print(a + b)
elif(choice == 2):
  print(a * b)
else:
  print("Invalid choice")
