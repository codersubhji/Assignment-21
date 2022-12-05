#7. Write a recursive python function to print squares of first N natural numbers

def square_Natural(num):
    if num>0:
        square_Natural(num-1)
        print(num**2 ,end=" ")

square_Natural(10)