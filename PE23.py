"""
Project Euler: Problem 23
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
An number n is called abundant if the sum of its proper divisors add to more than n. 
E.g. 12 is abundant, since 12 < 16 = 1+2+3+4+6.
"""

import math
import itertools

def sieve(N):
    """
    Return a boolean list is_prime where is_prime[i] is True iff i is prime,
    for 0 <= i < N, using the Sieve of Eratosthenes.
    """
    if N < 2:
        return [False] * N

    is_prime = [False, False] + [True] * (N - 2)
    limit = math.isqrt(N) + 1

    for p in range(2, limit):
        if is_prime[p]:
            # Start at p*p; smaller multiples are already marked
            for multiple in range(p * p, N, p):
                is_prime[multiple] = False
    return is_prime


def bool_list_to_primes(is_prime):
    """Convert a boolean prime list to a list of prime numbers."""
    return [i for i, flag in enumerate(is_prime) if flag]


def primes_below(N):
    """Return a list of all primes < N."""
    return bool_list_to_primes(sieve(N))


# Global prime list used for factorization
MAX_PRIME = 100_000
PRIMES = primes_below(MAX_PRIME)


def distinct_prime_factors(n):
    """
    Return a list of distinct prime factors of n.

    Uses the global PRIMES list. Assumes PRIMES is large enough to factor n.
    """
    factors = []
    temp = n
    i = 0

    # Trial division using PRIMES
    while i < len(PRIMES) and PRIMES[i] * PRIMES[i] <= temp:
        p = PRIMES[i]
        if temp % p == 0:
            factors.append(p)
            while temp % p == 0:
                temp //= p
        i += 1

    # If remaining temp > 1, it's a prime factor > sqrt(original n)
    if temp > 1:
        factors.append(temp)

    return factors


def prime_multiplicities(n):
    """
    Return the exponents of each distinct prime factor of n.

    Example: n = 12 = 2^2 * 3^1 -> [2, 1]
    """
    factors = distinct_prime_factors(n)
    exponents = []

    for p in factors:
        exp = 0
        temp = n
        while temp % p == 0:
            temp //= p
            exp += 1
        exponents.append(exp)

    return exponents


def divisors(n):
    """
    Return a list of all positive divisors of n.

    Uses prime factorization:
    n = p1^e1 * p2^e2 * ... -> all combinations of exponents 0...e_i.
    """
    factors = distinct_prime_factors(n)
    exponents = prime_multiplicities(n)

    # For each factor p_i with exponent e_i, create range(0, e_i + 1)
    exponent_ranges = [range(e + 1) for e in exponents]

    divs = []
    for exp_tuple in itertools.product(*exponent_ranges):
        d = 1
        for p, e in zip(factors, exp_tuple):
            d *= p ** e
        divs.append(d)

    return divs


def sum_of_proper_divisors(n):
    """Return the sum of all proper divisors of n (all divisors except n itself)."""
    divs = divisors(n)
    return sum(divs) - n


if __name__ == "__main__":
    LIMIT = 28_124

    # 1) Compute all abundant numbers < LIMIT
    abundant_numbers = []
    for n in range(1, LIMIT):
        s = sum_of_proper_divisors(n)
        if s > n:
            abundant_numbers.append(n)

    # 2) Compute all numbers that can be written as sum of two abundant numbers
    abundant_sums = []
    for a in abundant_numbers:
        for b in abundant_numbers:
            s = a + b
            if s < LIMIT:
                abundant_sums.append(s)

    abundant_sums_set = set(abundant_sums)
    all_numbers_set = set(range(LIMIT))

    # 3) Numbers that cannot be written as sum of two abundant numbers
    non_abundant_sums = all_numbers_set - abundant_sums_set

    total = sum(non_abundant_sums)
    print("Total sum of all numbers that cannot be written as sum of two abundant numbers:", total)
