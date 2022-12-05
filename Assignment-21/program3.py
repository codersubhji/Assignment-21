#3. Write a recursive python function to print first N odd natural numbers
def oddNatural(num):
    if num>0:
        oddNatural(num-1)
        print(num*2-1,end=" ")    


oddNatural(10)        