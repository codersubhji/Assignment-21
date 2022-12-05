#8. Write a recursive python function to print cubes of first N natural numbers
def cube_Natural(num):
    if num>0:
        cube_Natural(num-1)
        print(num**3, end=" ")

cube_Natural(10)