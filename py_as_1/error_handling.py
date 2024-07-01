def han(nm1, nm2):
    
    
    try:
        nm1 = int(nm1)
        nm2 = int(nm2)
        nm = nm1*nm2
    except TypeError:
        print("Error: please re enter")
    except ValueError:
        print("Error: different data type")
    else:
        return nm

num1 = input("Enter the first Number")
num2 = input("Enter the Second Number")
print("The Multiplication of two number is ",han(num1, num2),".")