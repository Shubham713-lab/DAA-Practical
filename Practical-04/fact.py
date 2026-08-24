import time

# ===================
#       Iterative
# ===================

def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter a number: "))

start = time.perf_counter()
result = factorial_iterative(n)
end = time.perf_counter()

runtime = end - start

print("Factorial =", result)
print("Runtime =", runtime, "seconds")

# ===================
#      Recursion
# ===================
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = int(input("Enter a number: "))

start = time.perf_counter()
result = factorial_recursive(n)
end = time.perf_counter()

runtime = end - start

print("Factorial =", result)
print("Runtime =", runtime, "seconds")