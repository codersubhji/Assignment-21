#5. Write a recursive python function to print first N even natural numbers.
def even_Natural(num):
    if num>0:
        even_Natural(num-1)
        print(2*num ,end=" ")  

    
even_Natural(10)      