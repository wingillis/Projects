def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


nthdigit = raw_input("Please provide n for the nth number of the fibonacci sequence:\n")
try:
	nthdigit = int(nthdigit)
	print fib(nthdigit)
except:
	print "That was not a number. Exiting with error code 1"


