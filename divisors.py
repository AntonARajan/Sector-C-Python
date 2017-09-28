#!/usr/bin/python3
d=(int(input("Enter a Number:"))) # function integer used with a statement
b=1
for b in range(1,d):# adding a range for entered number
	if(d%b==0):
		print(b)#prints if d is divisible by b
	
