print("Greeting!! Welcome to Calculator.")

num1 = int(input("Enter the First number:\n"))
num2 = int(input("Enter the Second Number:\n"))

print("Select the desired Operation:\n \"1. Addtion\" \n \"2. Subtraction\" \n \"3. Multiplication\" \n \"4. Division\" \n")

ans = int(input())

print("\nThe answer is ")

if ans==1:
    print(num1+num2)
elif ans==2:
    print(num1-num2)
elif ans==3:
    print(num1*num2)
elif ans==4:
    print(num1/num2)
else:
    print("Error")