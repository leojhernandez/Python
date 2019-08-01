#a = ['Leonardo', 'is', 'a', 'analyst']
#
#for i in range(len(a)):
#    print (i, a[i])

#print range(-10,-100,-30)


#break and continue statements and else clauses on loops

#for n in range(2,10):
#    for x in range(2, n):
#        if n % x == 0:
#            print n, 'equals', x, '*', n//x
#            break
#    else:
#        print n, 'is a prime number'



# Continue statement
#for num in range (2,10):
#    if num % 2 == 0:
#        print 'Found an even number', num
#        continue
#    print 'Found a number', num

# Defining Functions

#We can create a function that writes 
#the Fibonacci series to an arbitrary boundary

#def fib(n):
#    """ Print a Fibonacci series up to n."""
#    a,b = 0, 1
#    while a < n:
#        print a
#        a, b = b, a+b
#    
#fib(2000)

#def fib2(n):
#    """ Print a Fib series up to n. """
#    result = []
#    a, b = 0, 1
#    while a < n:
#        result.append(a)
#        a, b = b, a+b
#    return result 
#
#fib100 = fib2(100)
#print fib100
#


#def make_incrementor(n):
#    return lambda x: x + n
#
#f = make_incrementor(30)
#
#print f(1)

#squares = []
#for x in range(10):
#    squares.append(x**2)
#    
#print squares

#squares = [x**2 for x in range(10)]
#print squares 

#combs = [(x,y) for x in [1,2,3] for y in [3,4,1] if x!= y]
#print combs 

#vec = [-4, -2, -1, 0, 1, 2, 4]

# multuply vec by 2
#print [x*2 for x in vec]

# print only positive values
#print [x for x in vec if x >= 0]

# print all abs values
#print [abs(x) for x in vec]

# create a list of 2-tuples like (number, square)
#print [(x, x**2) for x in range (10)]

#vec = [[1,2,3], [4,5,6], [7,8,9]]
#
#print [x for elem in vec for x in elem]

matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 13]
        ]

#print [[row[i] for row in matrix] for i in range(4)]

#transposed = []
#for i in range(4):
#    transposed.append([row[i] for row in matrix])
#
#print transposed

#print list(zip(*matrix))


#knights = {'Gallahad': 'the pure', 'Robin': 'the brave'}
#
#for k, v in knights.items():
#    print k, v 


