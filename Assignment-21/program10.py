#10. Write a recursive python function to print a number in reverse order.

def rev_Number(num):
    if num<=0:
        return
    else:
        print(num, end=" ")

        rev_Number(num-1)

rev_Number(10)        