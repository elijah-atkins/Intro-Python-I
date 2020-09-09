# 3. Write a program to determine if a number, given on the command line, is prime.

#    1. How can you optimize this program?
#    2. Implement [The Sieve of
#       Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
#       of the oldest algorithms known (ca. 200 BC).

x = int(input("Is it prime: "))

# If num is divisible by any number between 2 and sqrt(n), it is not prime  

if x > 1:
    for i in range(2,int(x)):
        if (x % i) == 0:
            print(x, "is not a prime number")
            print(i, "times", x//i,"is", x)
            break
    else:
            print(x, "is a prime number")
else:
    print(x, "is not a prime number")
