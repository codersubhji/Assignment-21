#1. Write a recursive python function to print first N natural numbers.

def ntr(n):
    if n>0:
        ntr(n-1)
        print(n,end=" ")
       
    
ntr(10)   
    
    
   


        
