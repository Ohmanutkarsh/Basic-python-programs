import time,sys

while True:
    choice = input('write / read / add \n')
    if choice == 'write':
        f = open("ToDo_List.txt" , "w")
        while True:
            event = input("enter do's / write done if you are done \n")
            if event != 'done':
                f.write(event + "\n")
            else :
                break
        f.close()

    elif choice == 'read':
        f = open("ToDo_List.txt" , "r")
        i = 1
        for line in f:
            print(str(i) + ' ' + line)
            i += 1

        f.close()

    elif choice == 'add':
        f = open("ToDo_List.txt" , "a")
        while True:
            event = input("enter do's / write done if you are done \n")
            if event != 'done':
                f.write(event + '\n')
            else :
                break
        f.close()

    else:
        print("invalid option")

