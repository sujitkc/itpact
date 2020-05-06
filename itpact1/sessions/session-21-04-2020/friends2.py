vidyut = int(input("Enter Vidyut's contribution: "))
diva   = int(input("Enter Diva's contribution: "))
vigyan = int(input("Enter Vigyan's contribution: "))
udayan = int(input("Enter Udayan's contribution: "))
kashika = int(input("Enter Kashika's contribution: "))

total = vidyut + diva + vigyan + udayan + kashika

average = total / 5

print("Vidyut owes ", average - vidyut)
print("Diva owes ", average - diva)
print("Vigyan owes ", average - vigyan)
print("Udayan owes ", average - udayan)
print("Kashika owes ", average - kashika)
