# ----------------------------------------
# 1. Fibonacci Series
# ----------------------------------------
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # newline


# ----------------------------------------
# 2. Palindrome Number
# ----------------------------------------
def is_palindrome(num):
    return str(num) == str(num)[::-1]


# ----------------------------------------
# 3. Factorial (Recursive)
# ----------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ----------------------------------------
# 4. Reverse a String
# ----------------------------------------
def reverse_string(s):
    return s[::-1]


# ----------------------------------------
# 5. Check Prime Number
# ----------------------------------------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# ----------------------------------------
# 6. Find Largest Element in a List
# ----------------------------------------
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


# ----------------------------------------
# 7. Sum of Digits of a Number
# ----------------------------------------
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    # Fibonacci
    print("Fibonacci (7 terms):")
    fibonacci(7)

    # Palindrome
    print("\nPalindrome Check:")
    print("121:", is_palindrome(121))  # True
    print("123:", is_palindrome(123))  # False

    # Factorial
    print("\nFactorial:")
    print("5! =", factorial(5))  # 120

    # Reverse String
    print("\nReverse String:")
    print("hello ->", reverse_string("hello"))

    # Prime Check
    print("\nPrime Check:")
    print("29:", is_prime(29))  # True
    print("10:", is_prime(10))  # False

    # Largest in List
    print("\nLargest Element in List:")
    print(find_max([3, 7, 2, 9, 5]))  # 9

    # Sum of Digits
    print("\nSum of Digits:")
    print("1234 ->", sum_of_digits(1234))  # 10
