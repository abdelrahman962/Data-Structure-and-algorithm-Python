import operator



def Postfix(value):
    stack_call=[]   
    arithmetics={
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
    }
    for i in value:
        if i not in arithmetics:
            stack_call.append(float(i))
        else:
            b=stack_call.pop()
            a=stack_call.pop()
            result=arithmetics[i](a,b)
            stack_call.append(result)

    return  int(stack_call.pop())        
         




tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(Postfix(tokens))






