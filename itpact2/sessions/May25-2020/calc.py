choice = int(input("Enter your choice: "))

# A comment is a line that starts with a hash ('#') symbol.
# A comment is not considered by Python as part of the program text.
# But it can be read by the human reader.
# Hence, comments can be used to add explanatory notes to your program
# which may be helpful for the reader to understand your code.
# Just like this one

 answer = 0
if(choice == 1):
  print("Adding 10 and 5 ...")
  answer = 10 + 5
else:
  if(choice == 2):
    print("Subtracting 10 and 5 ...")
    answer = 10 - 5
  else:
    print("Nothing happened.")
print(answer)

# Don't get annoyed by errors because ...
# Errors अच्छे हैं! 
