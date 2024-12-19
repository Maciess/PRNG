import numpy as np

def lcg(m, a, c, x):
    return (a * x + c) % m

def get_n_lcg(m, a, c, init, size):
    result = np.empty(size, dtype=np.uint32)
    assert size >= 1, "Incorrect size"
    result[0] = lcg(m, a, c, init)
    for i in range(1, size):
        result[i] = lcg(m, a, c, result[i - 1])
    return result


def generalized_lcg(m, a, x):
    return np.sum(a * x) % m


def excell_gen(x):
    return (0.9821 * x + 0.211327) % 1


if __name__ == '__main__':
    a = np.array([3, 7, 68])
    x = np.array([3, 5, 6])
    rand = generalized_lcg(2 ** 10, a, x)
    print(rand)
