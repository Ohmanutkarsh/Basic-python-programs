import time,sys

while True:
    choice = input('1 write\n2 read\n3 add\n4 delete\n5 exit\n')
    if choice == 'write':
        with open("ToDo_List.txt" , "w") as f :
            while True:
                event = input("enter do's / write done if you are done \n")
                if event != 'done':
                    f.writelines(event + "\n")
                else :
                    break

    elif choice == 'read':
        with open("ToDo_List.txt" , "r") as f :
            lines = f.readlines()
            if not lines :
                print('no tasks awailable')
            else :
                for i, line in enumerate(lines):
                    print((i + 1), line.strip())

    elif choice == 'add':
        with open("ToDo_List.txt" , "a") as f :
            while True:
                event = input("enter do's / write done if you are done \n")
                if event != 'done':
                    f.writelines(event + '\n')
                else :
                    break

    elif choice == 'delete':
        with open("ToDo_List.txt" , "r") as f :
            lines = f.readlines()
            if not lines :
                print('no tasks available')
                continue
            else :
                for i, line in enumerate(lines):
                    print((i + 1), line.strip())

        while True:
            index = input('which index of task you want to delete / write 0 once you are done \n')
            try :
                ind = int(index)
            except ValueError :
                print('enter valid index')
                continue

            if ind > len(lines) or ind < 0:
                print('enter valid index')
                continue
            elif ind == 0 :
                break
            else:
                del lines[ind - 1]
                with open("ToDo_List.txt" , "w") as f :
                    f.writelines(lines)

                print('task number ' + str(ind) +' is deleted')


    elif choice == 'exit':
       sys.exit()

    else:
        print("invalid option")

