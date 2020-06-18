import sys

dec = input("Enter your decorator: ")
if(len(dec) != 1):
  print("Your decorator must be only one character long.")
  sys.exit(0)

msg = input("Enter your message: ")
l = len(msg)
decorator = dec * (l + 4)
print(decorator)
print(dec + " " + msg + " " + dec)
print(decorator)

