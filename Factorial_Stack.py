def factorial(n):
    stack_call=[]
    result=1
    while n:
        stack_call.append(n)
        n-=1

    while stack_call:
        temp=stack_call.pop()
        result*=temp

    return result



print(factorial(5))