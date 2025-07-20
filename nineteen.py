# Print Alternate Prime Numbers

def prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
            else:
                return True
    return

def alternatePrime(limit):
    primeNum = []
    for num in range(2, limit+1):
        if prime(num):
            primeNum.append(num)
    alternate = primeNum[::2]
    print(f"Alternate prime numbers to {limit}: {alternate}")

limit = int(input("Enter a limit: "))
alternatePrime(limit)


