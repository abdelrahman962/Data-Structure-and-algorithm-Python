import time

def fibo(n):
    if n==0 or n==1:
        return 1
    return fibo(n-1) + fibo(n-2)

#index  0 1 2 3 4 5 6
#value: 1 1 2 3 5 8 13
#dictionary

def fibo_better(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    start_timetime = time.time()
    for _ in range(2, n + 1):
      
        a, b = b, a + b
    end_time = time.time()
    print(f"Time taken : {end_time - start_timetime:.10f} seconds")
    return b

def fibo_Dictionary(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]





print(fibo_better(4))