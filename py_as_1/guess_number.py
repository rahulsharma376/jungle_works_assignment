print("******* Welcome to Guess the Number Game ******* :\n\n")

def guess():
    start = 1
    End = 1000
    
    print("Think of a Number between 1 to 1000:")
    
    while True:
        
        mid = (start+End) // 2  # used // for integer value    
        print("Is the number [y/n] or [Y/N]", mid,":\t")
        ch = input()
        if ch == ('y' or 'Y'):
            print("Congrats! You guessed the number ",mid)
            break
        elif ch == ('n' or 'N'):
            ch = input("Enter\n\t's' if number is smaller\n\t'h' if number is higher\n\t'c' if correct:\nPlease Enter your Choice [s|h|c] or [S|H|C]:\n")
            if ch == ('s' or 'S'):
                End = mid-1
            elif ch == ('h' or 'H'):
                start = mid+1
            elif ch == ('c' or 'C'):
                print("Congrats! You guessed the number ",mid)
                break
            else:
                print("Wrong Input. Please re-enter.")
    
guess()         