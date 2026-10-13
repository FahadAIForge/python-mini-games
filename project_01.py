import random 
n = random.randint(1,100)

a = -1
gusses = 0
while(a != n):
    gusses += 1 
    a = int(input("Guss a number : "))
    if ( a > n ):
        print("Lower number please : ")
    else:
        print("Heigher number please : ")
        
        
print(f"You have gussed the number {n} correctly in {gusses} attempt")