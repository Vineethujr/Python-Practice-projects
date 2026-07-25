# Even/Odd & Prime Number Checker

num = int(input("Enter a number: "))

# Even or Odd Checker
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Prime or Not Prime Ckecker
if num <= 1:
    print(num, "is Not a Prime Numbe")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is Not a Prime Number")