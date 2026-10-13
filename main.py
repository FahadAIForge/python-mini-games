import random
'''
1 for snake 
-1 for water 
o for gun 
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice  : ")
youdict = {"s":1,"w":-1,"g":0}
reverseddict = {1: "Snake",-1: "Water", 0:"Gun"}
you = youdict[youstr]

print(f"You choice {reverseddict[you]}\ncomputer choice {reverseddict[computer]}")

if (computer == you):
    print("Draw : ")

else:  
    if(computer == -1 and you == 1):
        print("you win!")
        
    elif(computer == -1 and you == 0):
        print("you loss!")
        
    elif(computer == 1 and you == -1):
        print("you loss!")
        
    elif(computer == 1 and you == 0):
        print("you win!")
        
    elif(computer == 0 and you == 1):
        print("you loss!")
        
    elif(computer == 0 and you == -1):
        print("you win!")
        
    else:
        print("Some thing went wrong : ")