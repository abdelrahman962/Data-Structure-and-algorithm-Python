from StackList import StackList


def is_balance(Parentheses):
    opened=["(","[","{"]
    closed=[")","]","}"]
    stack=StackList()
    for i in Parentheses:
        if i in opened:
            stack.push(i)
        elif i in closed:
            if stack.top is None:
                return False
            
            index=closed.index(i)
            if stack.top.data==opened[index]:
                stack.pop()

            else:
                return False
    if stack.top==None:
        return True
    return False            



Parentheses=input("Enter Parentheses: ")
print(is_balance(Parentheses))