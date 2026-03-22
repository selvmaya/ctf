import string
import random
import math

alphabet = "abcdefghijklmnopqrstuvwxyz"

phi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2
sqrt5 = math.sqrt(5)


def fib_closed(n):
    """
    Compute F_n using the closed-form expression.
    Valid for moderate n (educational use).
    """
    return int(round((pow(phi, n, len(alphabet)) - pow(psi, n, len(alphabet))) / sqrt5))


def fib(n, mod):
    def _fib(k):
        if k == 0:
            return (0, 1)
        a, b = _fib(k >> 1)
        c = (a * ((b << 1) - a)) % mod
        d = (a * a + b * b) % mod

        # where values of k are odd
        if k & 1:
            return (d, (c + d) % mod)
        else:
            return (c, d)

    return _fib(n)[0]


# find
def fib_caesar_encrypt(n, text):
    # find some starting values
    a = fib(n, len(alphabet))
    b = fib(n + 1, len(alphabet))

    # shift values by a fibbonaci amount per letter position
    out = []
    for c in text:  # every letter corresponds to an output letter, length unchanged
        if c in string.whitespace:  # whitespace unchanged
            out.append(c)
            continue
        k = a % len(alphabet)
        a, b = b, a + b
        # is this just a really complicated way to figure out how much to caesar shift?
        out.append(alphabet[(alphabet.index(c) + k) % len(alphabet)])
    return "".join(out)


def fib_caesar_decrypt(a, b, cyphertext):

    out = []
    return "".join(out)


# a possible ways to solve:
# - decrypt letters using decomposition of fib numbers, and looking through results of decryption over all possible values of a and b, assuming b depends on a or that they are capped under length of the alphabet, which we already know
#
# what wouldn't work:
# - trying every key naively (0..2^128)


key = random.randint(0, 2**128)  # i cannot guess the key


def encrypt_main():
    # Danish text, flag is in text
    with open("flag.txt", "rb") as f:
        text = f.read().decode("utf-8").strip()

    ciphertext = fib_caesar_encrypt(key, text)
    print(ciphertext)

    with open("encryption.txt", "wb") as f:
        f.write(ciphertext.encode("utf-8"))

    # Once you have decrypted the ciphertext, remember to add flag formatting
    # For example:
    # ddc example flag
    # to
    # ddc{example_flag}


def decrypt_main():
    with open("./encryption.txt", "rb") as f:
        cyphertext = f.read().decode("utf-8").strip()

    m = len(alphabet)

    # we can make a semi-educated guess that both a and b are <= m, but that's still at least 26^2 options for our given cyphertext.

    # mod'd fib does not repeat as obviusly as I assumed.
    # And despite knowing that the input to fib for a and b are just 1 away, we don't know what the starting value is, and the two values diverge quite a bit, so we would still have to explore those 26^2=676 options.

    for n in range(0, m * 3):
        print(f"Fib (mod) of {n} (n mod m = {n % m}): {fib(n, m)}")


if __name__ == "__main__":
    # encrypt_main()
    decrypt_main()
