

class PrimeNumber(object):

    @staticmethod
    def is_prime(n):
        """
        this function is to check number is prime number or not
        :param n: number
        :return:
        """
        if n <= 1:
            return False
        for x in range(2, int(n/2)+1):
            if n % x == 0:
                return False
        else:
            return True

    @staticmethod
    def is_prime_old(number):
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True

    @staticmethod
    def get_list_prime(number):
        start_number = 2
        prime_list = [start_number]
        for x in range(start_number, number):
            if PrimeNumber.is_prime(x):
                prime_list.append(x)
        return prime_list
