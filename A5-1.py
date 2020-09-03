num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int

    num_int = int(input("Input a number: "))    # Do not change this line
else: 
    print("The maximum is", max_int) 


    # 2

n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = 1
num2 = 2
num3 = 3

print(num1, num2, num3, end='')

for n in range(1, n-2):
    summa_int = 0
    summa_int = summa_int+num1+num2+num3

    num1=num2
    num2=num3
    num3=summa_int

    print(num3, end='')