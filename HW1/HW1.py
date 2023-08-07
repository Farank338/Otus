def print_spell(print_eq):
    for x in range(25):
        for y in range(25):
            if print_eq(x,y)==True:
                print('#',end=' ')
            else:
                print('.',end=' ')
        print()
        

def print_eq(x,y):return (x < y)
print('01. if (x > y)')
print_spell(print_eq)

def print_eq(x,y):return (x == y)
print('02. if (x == y)')
print_spell(print_eq)

def print_eq(x,y):return (x == 24 - y)
print('03. if (x == 24 - y)')
print_spell(print_eq)

def print_eq(x,y):return (x + y < 30)
print('04. if (x + y < 30)')
print_spell(print_eq)

def print_eq(x,y):return (int(x / 2) == y)
print('05. if (Math.floor(x / 2) == y)')
print_spell(print_eq)

def print_eq(x,y):return (x < 10 or y < 10)
print('06. if (x < 10 || y < 10)')
print_spell(print_eq)

def print_eq(x,y):return (x > 15 and y > 15)
print('07. if (x > 15 && y > 15)')
print_spell(print_eq)

def print_eq(x,y):return (x * y == 0)
print('08. if (x * y == 0)')
print_spell(print_eq)

input()