n = int(input("input n"))

def fibonacci(n):
    if n>2:
        return fibonacci(n-1)+fibonacci(n-2)        #repeat the function with the 2 previous numbers
    else:
        return 1    #when done return 1 (the final number)

print(fibonacci(n))
