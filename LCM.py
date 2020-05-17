print("Enter 2 integers numbers:\n")
a=int(input("1st no."))
b=int(input("2nd no."))

if a>b:
	least=b

if a<b:
	least=a

while 1:
	if least % a==0 and least % b==0:
		print("The lcm is ",least)
		break
	least=least+1
