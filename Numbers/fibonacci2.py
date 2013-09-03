def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    c=0
    while c < n:
#        print b,
        a, b = b, a+b
        c+=1
#    print '\n'
    return a

i=0
j=0
while i<1000:
    j+=1
    i = len(str(fib(j)))

print j, '\n', fib(j)
