#!/usr/bin/env python3
import ipdb

def print_fibonacci(length):
    fib = []
    i=0
    while i < length:
        if i==0 or i==1:
            fib.append(i)
        elif length == 0:
            pass
        else:
            fib.append(fib[i-1] + fib[i-2])
        i+=1
    print(fib)

# ipdb.set_trace()