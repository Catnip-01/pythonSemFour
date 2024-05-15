def fib():
    a = 0
    b = 1
    x = a + b
    while (x < 100):
        x = a + b
        if x < 100:
            print(x)
        a = b
        b = x
        
        
fib()