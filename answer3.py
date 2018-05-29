l1=[]
l2=[]
ch='y'
while ch=='y':
	e=int(input("Enter an integer input: "))
	l1.append(e)
	l2.append(e**2)
	ch=input("Want to enter more integers? y//n")

print("You entered the following integers: ")
print(l1)
print("The squares of entered integers are: ")
print(l2)

