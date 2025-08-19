
def Infix(infex_expresion):
    values=infex_expresion.split()
    stack_list=[]
    postfix=[]
    operators={
    '(':0,
    ')':0,
    '+':1,
    '-':1,
    '*':2,
    '/':2

    }

    for i in values:
        if i.isnumeric():
            postfix.append(i)
        elif i=='(':
            stack_list.append(i)
        elif i==')':
            while stack_list and stack_list[-1]!='(':
                postfix.append(stack_list.pop())
            stack_list.pop()
        else:
            while stack_list and operators.get(i,0)<=operators.get(stack_list[-1],0):
                postfix.append(stack_list.pop())
            stack_list.append(i)    

    while stack_list:
        postfix.append(stack_list.pop())     
            

    return ' '.join(postfix)





infex_expression1="( 1 + 2 ) * 3"
infex_expression2="( 1 + 2 ) * ( 3 + 4 )"

print(Infix(infex_expression1))
print(Infix(infex_expression2))
