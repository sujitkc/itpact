# Input a message from user.
# Print this message 10 times.
# Use a loop.
# If we don't increment of counter then 
# the loop runs endlessly.
# Such loops are called 'infinite loops.'
# To force a program to stop executing, press ctrl-c.

msg = input("Enter your message: ")

count = 0
while(count < 10):
  print(msg)
  count = count + 1
  print("count = ", count)

print("Quitting ...")
