top=None
people = []

def push(stack, item):
    global top
    stack.append(item)
    top = len(stack)-1

def peek(stack):
    if top!=None:
        return stack[top]
    else:
        return 'underflow'

def pop(stack):
    global top
    if top!=None:
        stack.pop()
        top = len(stack)-1
        print(top)
    else:
        return "underflow"

def display(stack):
    print(top)
    if top!=None:
        for i in stack[::-1]:
            print(i)
    else:
        return 'underflow'

while True:
    choice = int(input(" 1. if u want to add elements \n 2. if u want to delete element \n 3. if u want to display full list \n 4. if u want to peek \n 5. if u want to exit\n "))

    if choice == 1:
        push(people,[input("enter name of person "),int(input("enter age"))])

    if choice == 2:
        pop(people)

    if choice == 3:
        print(display(people))

    if choice == 4:
        print(peek(people))

    if choice == 5:
        break
