#!/usr/bin/python3
import random
r=random.randint(15,45) # gives random num
print(r)
if r<25:
  print(r)
  print(": is less than 25")
elif r==27:
	print("27 is a multiple of 3 and 9, both")
elif r>=30:
	print("is greater than 30")
else:
	print("your number is: ", r)