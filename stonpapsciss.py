#!/usr/bin/python3
import random
t=["Scissors","Paper","Rock"]
Ubuntu=t[random.randint(0,2)]
My_choice="False"
while My_choice=="False":
	if(My_choice==Ubuntu):
		print("Tie")
		elif(My_choice=="Paper"):
			if(Ubuntu=="Rock"):
				print("You Win!!", My_choice, "covers" ,Ubuntu)
			else:
				print("You Lose:(", Ubuntu, "smashes" ,My_choice)
	    elif(My_choice=="Scissors"):
	    	if(Ubuntu=="Paper"):
	    		print("You Win!!", My_choice, "cuts" ,Ubuntu)
		 	else:
		 		print("You Lose", Ubuntu, "covers" ,My_choice)
		elif(My_choice=="Rock"):
			if(Ubuntu=="Scissors"):
				print("You Win!!", My_choice, "smashes" ,Ubuntu)
			else:
				print("You Lose", Ubuntu, "cuts" ,My_choice) 
		
