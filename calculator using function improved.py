import sys, time

history=[]




def calculate(a ,operation, b):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '/':
        try :
            c = a/b
            return c
        except ZeroDivisionError:
            return "Error: Division by zero"
    elif operation == '**':
        return a**b
    elif operation == '%':
        return a%b
    else :
        print("please select an apropriate operation")


def continuation(ans) :
    while True:

        a = ans
        print(ans)
        operation = input("enter operation ")
        if operation == 'history':
            if not history :
                print('no history yet')
            else:
                for item in history:
                    print(item)
            continue

        if operation == 'exit':
            break

        if operation not in ['+','-','*','/','**','%']:
            print('enter apropriate operation')
            continue
        try :

            b = int(input("enter second number "))
            ans = calculate(a, operation, b)
            print("answer is", ans ,"\n")
            history.append(f"{a} {operation} {b} = {ans}")

        except ValueError:
            time.sleep(0.7)
            print("You didn't entered the numbers , enter the numbers \n")
            continue

        print("do you want to continue with", ans, "? (if yes type y if no type anything )")
        con2 = input()
        if con2 == 'y':
            continue
        else :
            break





while True:
    use = input("do you want to use the calculator , say y or n \n")
    if use == 'y':
        time.sleep(0.7)
        print("use the operation \n + = addition \n - = subtraction \n * = multiplication \n / = division \n ** = exponential \n % = remainder \n exit = exit \n history = history \n")

        operation = input("enter operation ")

        if operation == 'history':
            if not history :
                print('no history yet')
            else:
                for item in history:
                    print(item)
            continue

        if operation == 'exit':
            sys.exit()

        if operation not in ['+','-','*','/','**','%']:
            print('enter apropriate operation')
            continue

        try :

            a = int(input("enter first number "))
        except ValueError:
            time.sleep(0.7)
            print("You didn't entered the number, enter the number \n")
            continue
        try :
            b = int(input("enter second number "))
        except ValueError:
            time.sleep(0.7)
            print("You didn't entered the number, enter the number \n")
            continue


        ans = calculate(a, operation, b)
        print("answer is", ans ,"\n")
        history.append(f"{a} {operation} {b} = {ans}")

        print("do you want to continue with", ans, "? (if yes type y if no type anything )")
        con1 = input()
        if con1 == 'y' :
            continuation(ans)

        else :
            continue

    elif use == 'n':
        sys.exit()
    else :
        print('enter apropriate input')



