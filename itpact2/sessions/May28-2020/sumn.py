# Write a program that computes the sum of first n positive integers.
# 1 + 2 + ... + n = n (n + 1) / 2 ====> Prove this.


n = int(input("Enter the number: "))

count = 1
mysum = 0

# One execution of the body of the loop is called one "iteration"
# Control flow instruction
while(count <= n):
  print(mysum, count)
  mysum = mysum + count # incrementation by count
  count = count + 1  # incrementation by 1.

print("sum = ", mysum) 
