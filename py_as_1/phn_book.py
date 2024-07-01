def viewContact():
    # print(contacts)
    print("All Contacts:\n")
    for item in contacts:
        print(item, " : ", contacts[item])
    choc = input("Do you want to contiue go to main page or exit [Y/N]:\n")
    if choc == ('n' or 'N'):
        exit("\nThank you for using Phone Application, Exiting.")

def addContact():
    while True:
        name = input("Enter the Name of the Person:\t")
        while name in contacts:
            print("Please use different name:\n")
            name = input()
            
        ph = int(input("Enter the phone number:\t"))
        contacts[name] = ph;
        choc = input("Do you want to add more contacts [Y/N]:\n")
        if choc == ('n' or 'N'):
            break
    

def searchContact():
    while True:
        name = input("Enter the Name of the Person:\t")
        if name in contacts:
            print("Contact Found:\n", name," : ",contacts[name])
        else:
            print("Contact Not Found.\n")
        choc = input("Do you want to search more or not[main page] [Y/N]:\n")
        if choc == ('n' or 'N'):
            break

def deleteContact():
    while True:
        name = input("Enter the name of the Person:\n")
        if name in contacts:
            del contacts[name]
        print("Contact Deleted.")
        choc = input("Do you want to delete more or not[main page] [Y/N]:\n")
        if choc == ('n' or 'N'):
            break

contacts = {}

# This code will run infinite until user exit. 
while True:
    print("Select from below:\n     1. View Contact\n     2. Add Contact\n     3. Search Contact\n     4. Delete Contact\n     5. Exit\n    ")
    
    ch = int(input("Enter your choice:\n"))
    
    if ch == 1:
        viewContact()
    elif ch == 2:
        addContact()
    elif ch == 3:
        searchContact()
    elif ch == 4:
        deleteContact()
    elif ch == 5:
        print("Good Bye, Exiting the Phone Book Application.")
        break
    else:
        print("Invalid Input. Please Retry.")