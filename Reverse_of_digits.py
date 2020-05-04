n=int(input("Enter an integer:"))
reverse=0
while n!=0:
	rem=n%10
	reverse = reverse * 10 + rem
	n=n/10

print("The reverse is ",reverse)
