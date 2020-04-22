print("I'm a caluculator")
print("Enter 2 numbers:")

a=int(input("First number please: "))
b=int(input("second number please: "))

d=int(input("Tell me your selection:\n1.Add\n2.Sub.\n3.Mul.\n4.Div\n"))


if d==1:
	c=a+b


elif d==2:
	c=a-b
	

elif d==3:
	c=a*b
	

elif d==4:
	c=a/b
	

else:
	print("LOL the options are 1 to 4 😂️")

print("result= ",c)
