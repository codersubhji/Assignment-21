"""6. Write a recursive python function to print first N even natural numbers in reverse
order."""

def rev_even_Natural(num):
    if num<=0:
        return
    else:
        print(2*num ,end=" ")

        rev_even_Natural(num-1)

rev_even_Natural(10)