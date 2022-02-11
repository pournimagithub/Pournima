print("1.Check if Number is Prime or Not")
print("2.Calculate factorial of given number")
print("3.Given number is palindrome or not")
print("4.given number is armstrong or not")
print("5.Exit Prog")


def prime():
    Num = int(input(" Please Enter any Num: "))
    count = 0
    i = 2

    while i <= Num // 2:
        if i == 0:
            count = count + 1
            break
        i = i + 1

    if count == 0 and Num != 1:
        print(" %d is a Prime" % Num)
    else:
        print(" %d is not a Prime" % Num)


def factorial():
    num = int(input("\nEnter a number: "))
    fact = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            fact = fact * i
        print("The factorial of", num, "is", fact)


def palindrome():
    n = int(input("\nEnter number:"))
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev:
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")


def armstrong():
    num = int(input("\nEnter Number="))
    sum1 = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum1 += digit ** 3
        temp //= 10
    if num == sum1:
        print(num, "is an Armstrong Number")
    else:
        print(num, "is not an Armstrong Number")


def ex():
    exit(0)


def default():
    print("Wrong Choice Try again!")


a = 0
while a == 0:
    ch = int(input("Enter Choice: "))
    if ch == 1:
        prime()
    elif ch == 2:
        factorial()
    elif ch == 3:
        palindrome()
    elif ch == 4:
        armstrong()
    elif ch == 5:
        ex()
    else:
        default()
