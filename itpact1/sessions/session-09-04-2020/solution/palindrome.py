import sys

s = input("Enter the string: ")

rev_s = ""
l = len(s)

i = 0
while(i < l):
  rev_s = rev_s + s[l - 1 - i]
  i = i + 1

print("rev_s = ", rev_s)

i = 0
while(i < l):
  if(s[i] != rev_s[i]):
    print("Not a palindrome")
    sys.exit(0)
  i = i + 1

print("Palindrome")
