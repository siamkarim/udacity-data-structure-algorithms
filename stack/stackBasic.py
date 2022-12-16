stack = []
def push ():
    if len(stack)==n:
        print("your stack is full")
    else:
        element = input("Enter the Element:")
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("stack is empty")

    else:
        e = stack.pop()
        print("remove element:",e)
        print(stack)
n = int(input("Enter your limit"))
while True:
    print(" Select the operation 1.Push 2. pop 3. Quit")

    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break

    else:
        print("Enter the correct operation")
