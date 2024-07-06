def factorial(n):
    if n == 1:
        return 1
    else:
        print(f"N iterating {n}")
        return n * factorial(n - 1)

print(f"{factorial(6)}")