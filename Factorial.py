
a=int(input("Enter a number"))
fact = 1
if a==0:
	print("Factorial is 1")
elif a<0:
	print("Enter a +ve no.")
	
for i in range(1, a+1):
    fact=fact*i
print(fact)


