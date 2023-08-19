def get_circular_permutations(number):
    number_str = str(number)
    length = len(number_str)
    circular_permutations = []

    for i in range(length):
        permutation = int(number_str[i:] + number_str[:i])
        circular_permutations.append(permutation)

    return circular_permutations


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_primes_from_circular_permutations(number):
    circular_permutations = get_circular_permutations(number)
    prime_circular_permutations = []

    for permutation in circular_permutations:
        if is_prime(permutation):
            prime_circular_permutations.append(number)

    return prime_circular_permutations


# Example usage:
number = 1193
prime_circular_permutations = get_primes_from_circular_permutations(number)
print(prime_circular_permutations)
