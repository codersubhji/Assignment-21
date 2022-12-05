#9. Write a recursive python function to print first N multiples of a given number.

def first_n_multiple(num):
    if num>0:
        first_n_multiple(num-1)
        print(num * n, end=" ")
        
        
n=int(input("Enter any number for multiply..:"))
first_n_multiple(10)        