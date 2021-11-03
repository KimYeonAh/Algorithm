def fib_dp_mem(n) :
    if mem[n] == None :
        if n < 2 :
            mem[n] = n
        else :
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]

n = 8
mem = [None]*(n+1)
print('Fibonacci(%d) = '%n, fib_dp_mem(n))
