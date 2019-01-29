def is_prime(number):
    for num in range(number):
        if number % 2 == 0:
            return False
    return True