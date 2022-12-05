#2. Write a recursive python function to print first N natural numbers in reverse order
def revNatural(num):
    if num <=0:
        return
    else:
        print(num,end=" ")
        
        revNatural(num-1)
     


revNatural(10)     