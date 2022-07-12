# Problem 70:
#     Totient Permutation
#
# Description:
#     Euler's Totient function, φ(n) [sometimes called the phi function],
#       is used to determine the number of positive numbers less than or equal to n which are relatively prime to n.
#     For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9) = 6.
#     The number 1 is considered to be relatively prime to every positive number, so φ(1) = 1.
#
#     Interestingly, φ(87109) = 79180, and it can be seen that 87109 is a permutation of 79180.
#
#     Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

from collections import defaultdict
from typing import Tuple


def is_permutation(x: int, y: int) -> bool:
    """
    Returns True iff `x` and `y` are permutations of each other's digits.

    Args:
        x (int): Natural number
        y (int): Natural number

    Returns:
        (bool): True iff `x` and `y` are permutations of each other

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(x) == int and x > 0
    assert type(y) == int and y > 0

    # Count digits in `x`
    digits = defaultdict(lambda: 0)
    s = str(x)
    for d in s:
        digits[d] += 1

    # Check if digits in `y` match
    s = str(y)
    for d in s:
        digits[d] -= 1
        if digits[d] < 0:
            return False
    return True


def main(n: int) -> Tuple[int, int, float]:
    """
    Returns the value of `x`,
      where 1 < x < `n`
      and φ(x) is a permutation of `x`,
      such that x/φ(x) is minimized.

    Args:
        n (int): Natural number, greater than 2

    Returns:
        (Tuple[int, int, float]):
            Tuple of ...
              * `x`, where 1 < x < `n` and φ(x) is a permutation of `x`, such that x/φ(x) is minimized
              * φ(x)
              * x/φ(x)

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 2

    # Value of totient at each index `i`
    # 0 and 1 aren't necessary, but kept for code readability
    phi = list(range(n))

    # Keep track of the best 'inverse totient ratio' while iterating
    x_best = phi_best = ratio_best = None

    # Sieve method using primes to calculate totient within this range
    for x in range(2, n):
        if phi[x] == x:
            # Found a prime, so use it to discount factors from later multiples
            for m in range(x, n, x):
                phi[m] -= phi[m] // x

        # Check if phi is a permutation
        # If so, compare inverse totient ratio
        if is_permutation(x, phi[x]):
            ratio = x / phi[x]
            if ratio_best is None or ratio < ratio_best:
                print('Found {}'.format(x))
                x_best = x
                phi_best = phi[x]
                ratio_best = ratio

    return x_best, phi_best, ratio_best


if __name__ == '__main__':
    upper_limit = int(input('Enter a natural number (greater than 2): '))
    best_n, best_phi, best_ratio = main(upper_limit)
    print('Value of `n`, where 1 < n < {},'.format(upper_limit))
    print('  where `φ(n)` is a permutation of `n`,')
    print('  having the least ratio `n/φ(n)`:')
    print('    n      = {}'.format(best_n))
    print('    φ(n)   = {}'.format(best_phi))
    print('    n/φ(n) = {:.10f}'.format(best_ratio))
