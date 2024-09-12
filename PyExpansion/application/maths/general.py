PRIME_START_NUMBER = 2


def is_prime(n):
    """
    this function is to check number is prime number or not
    :param n: number
    :return:
    """
    if n <= 1:
        return False
    for x in range(PRIME_START_NUMBER, int(n / PRIME_START_NUMBER) + 1):
        if n % x == 0:
            return False
    else:
        return True


def get_list_prime(number):
    prime_list = [PRIME_START_NUMBER]
    for x in range(PRIME_START_NUMBER, number):
        if is_prime(x):
            prime_list.append(x)
    return prime_list
