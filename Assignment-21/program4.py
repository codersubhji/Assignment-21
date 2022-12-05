#4. Write a recursive python function to print first N odd natural numbers in reverse order

def revOdd_natural(num):
    if num<=0:
        return
    else:
        print(2*num-1 , end=" ")

        revOdd_natural(num-1)
revOdd_natural(10)        