PRIME = 72057594037927931
DOMAIN = 128


def roll_hash(old_val, out_digit, in_digit, last_pos):
    val = (old_val - out_digit * last_pos + DOMAIN * PRIME) % PRIME
    val = (val * DOMAIN) % PRIME
    return (val + in_digit) % PRIME


def matches(s, t, i, j, k):
    for d in range(k):
        if s[i + d] != t[j + d]:
            return False
    return True


def rabin_karp_matching(s, t):
    hash_s = 0
    hash_t = 0
    len_s = len(s)
    len_t = len(t)
    last_pos = pow(DOMAIN, len_t - 1) % PRIME
    if len_s < len_t:
        return -1
    for i in range(len_t):
        hash_s = (DOMAIN * hash_s + ord(s[i])) % PRIME
        hash_t = (DOMAIN * hash_t + ord(t[i])) % PRIME
    for i in range(len_s - len_t + 1):
        if hash_s == hash_t:
            if matches(s, t, i, 0, len_t):
                return i
        if i < len_s - len_t:
            hash_s = roll_hash(hash_s, ord(s[i]), ord(s[i + len_t]), last_pos)
    return -1


if __name__ == '__main__':
    s = 'set/3q.kffgame.com.txt'
    t = '115/20_theatlantic.com.txt'
    result = rabin_karp_matching(s, t)
    print(result)
