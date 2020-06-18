# Three friends -- Amar, Akbar, and Anthony -- go out to watch movie.
#  Amar - 100
#  Akbar - 200
#  Anthony - 300
# Find average money spent by each of the friends.

'''
amar = 100
akbar = 200
anthony = 300
radha = 500
shabana = 450
julie = 150
'''

friends = [ 100, 200, 300, 500, 450, 150, 230, 670, 321, 4566 ]

total = 0
i = 0
while(i < len(friends)):
  total += friends[i] # same as total = total + friends[i]
  i += 1 # same as i = i + 1

average = total / len(friends)

print(average)

# To err is human and to forgive divine.
