def gcd_subtraction(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def gcd_modulo(a: int, b: int) -> int:
    # Euclidean algorithm using modulo
    while b:
        a, b = b, a % b
    return a


def gcd(a: int, b: int) -> int:
    # Knuth TAOCP Vol.2 §4.5.2 Algorithm B (Binary GCD)
    if a == 0:
        return b
    if b == 0:
        return a

    # B1: find k, the highest power of 2 dividing both u and v
    k = 0
    while (a | b) & 1 == 0:
        a >>= 1
        b >>= 1
        k += 1

    # B2: initialise t
    t = -b if (a & 1) else a

    while True:
        # B3/B4: halve t until odd
        while t & 1 == 0:
            t >>= 1

        # B5: reset max
        if t > 0:
            a = t
        else:
            b = -t

        # B6: subtract
        t = a - b
        if t == 0:
            break

    return a << k


def gcd_binary_unscaled(a: int, b: int) -> int:
    # Variant of Knuth Algorithm B using a bitmask instead of shifting a/b.
    # m = 2^k is the lowest bit shared by both a and b; used as the unit of
    # "oddness" throughout so the final << k rescale is not needed.
    if a == 0:
        return b
    if b == 0:
        return a

    s = a | b
    m = s & -s  # isolate lowest shared power of 2

    t = -b if (a & m) else a

    while True:
        while not (t & m):
            t >>= 1

        if t > 0:
            a = t
        else:
            b = -t

        t = a - b
        if t == 0:
            break

    return a
