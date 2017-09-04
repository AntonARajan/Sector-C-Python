#!/usr/bin/python3
import random
i=0
while(i<=100):
	p=input("press 4 to roll a dice: ")
	if p==4:
		r=random.randint(1,6) # gives a random integer
		i=i+r
		print("Your new position is" ,i)
		if i==13:
			i=34
			print("LUCKY! YOU JUST GOT UP A LADDER")
		elif i==11:
			i=2
			print("HARD LUCK, YOU'VE JUST BECOME A SNAKES MEAL")
        elif i==8:
            i=37
            print("LUCKY! YOU JUST GOT UP A LADDER")
        elif i==25:
            i=4
            print("HARD LUCK, YOU'VE JUST BECOME A SNAKES MEAL")
        elif i==38:
            i=9
            print("HARD LUCK, YOU'VE JUST BECOME A SNAKES MEAL")
        elif i==40:
            i=68
            print("LUCKY! YOU JUST GOT UP A LADDER")
        elif i==52:
            i=81
            print("LUCKY! YOU JUST GOT UP A LADDER")
        elif i==65:           
            i=46
            print("HARD LUCK, YOU'VE JUST BECOME A SNAKES MEAL")
        elif i==76:
            i=97
            print("LUCKY! YOU JUST GOT UP A LADDER")
        elif i==89:
            i=70
            print("HARD LUCK, YOU'VE JUST BECOME A SNAKES MEAL")
        elif i==93:
            i=64
            print("HARD LUCK, YOU'VE JUST BECOME A SNAKES MEAL")
    if i>=94:
        if i+r==100:
            print("Congratulation you have reach HOME")
        else
            print("Roll Again")
            
    
                
        
            


              
                
                   
                                   
                    
                    
		


                                   
                    
                    
		

		
	
