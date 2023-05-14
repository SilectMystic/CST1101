#Here it asks the user about the pay and the tip.
print("How much is your bill?")
p = input()
print()

print("How much do you want to tip in percentage?")
t = input()
print()

print("How many people will pay?")
B = input()
print()

#Using the numbers that the user used in the input command will be calculated and also changed their data type.
i = (int(t) / 100)
l = (float(p)*float(i))
A = (float(p)+float(l))
C = (float(A)/int(B))

#Here the command prints the result from the calculation.
print("The total amount would be: $" + str(A))
print("The tip would be: $" + str(l))
print("Amount of pay per person: $" + str(C))