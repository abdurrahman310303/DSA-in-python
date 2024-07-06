def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(f"iterating n {n}")
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(f"{fibonacci(12)}")