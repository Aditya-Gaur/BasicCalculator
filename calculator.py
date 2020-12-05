def add(x, y) :
    return(x + y)

def sub(x, y) :
    return(x - y)

def mul(x, y) :
    return(x * y)

def div(x, y) :
    return(x / y)

while True :
    try :
        x = float(input("Enter First No. - "))
    except:
        x = None
        print('Invalid input:(')
    
        while x != float:
            try:
                x = float(input('Enter the first number again - '))
                break
            except:
                print('Invalid input:(')
                continue
    
    try :
        y = float(input("Enter Second No. - "))
    except :
        y = None
        print('Invalid input:')
    
        while y != float:
            try:
                y = float(input('Enter the second number again - '))
                break
            except:
                print('Invalid input:(')
                continue

    op = input('Enter operation(+, -, *, /)')

    a = '+'
    s = '-'
    m = '*'
    d = '/'

    while op == a :
        print('The result is ',add(x, y))
        print(input('\nPress enter to continue'))
        break
    
    while op == s :
        print('The result is ',sub(x, y))
        print(input('\nPress enter to continue'))
        break

    while op == m :
        print('The result is ',mul(x, y))
        print(input('\nPress enter to continue'))
        break

    while op == d :
        print('The result is ',div(x, y))
        print(input('\nPress enter to continue'))
        break







    
