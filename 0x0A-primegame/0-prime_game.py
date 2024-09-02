#!/usr/bin/python3


def isWinner(x, nums):
    # Utility function to find primes up to max_n using Sieve of Eratosthenes
    def sieve_of_eratosthenes(max_n):
        is_prime = [True] * (max_n + 1)
        p = 2
        while (p * p <= max_n):
            if (is_prime[p] is True):
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, max_n + 1) if is_prime[p]]

    # Find the maximum n in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1  # Ben wins if n < 2 (no primes for Maria)
            continue

        remaining = n
        move_count = 0

        # Count how many prime numbers <= n
        prime_count = sum(1 for p in primes if p <= n)

        # If the number of primes is odd, Maria wins, otherwise Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
