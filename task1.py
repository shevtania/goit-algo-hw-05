def caching_fibonacci():
# create  dict cache    
    cache = {}
# create function for calc fibonacci    
    def fibonacci(n):
    # two trivial cases    
        if n <= 0:
            return 0
        elif n == 1:
            return 1
    # check if n already in cache => return this value    
        elif n in cache:
            return cache[n]
    # if fibonachi(n) is absent in cache => we calculate it and put it in the cache    
        cache[n] = fibonacci(n - 2) + fibonacci(n - 1)
        return cache[n]
    # return inner function
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))