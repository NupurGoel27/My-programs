
def fib(n):
    a=0
    b=1
    if n==1:
        print(n)
    elif n<1:
        print("NOt a valid number. Please enter positive number: ")
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if c>100:
                break
            print(c)
fib(100)