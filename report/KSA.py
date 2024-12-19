import numpy as np


class Keys:
    def __init__(self, keys: np.ndarray):
        self.num_of_keys = keys.shape[0]
        self.keys = keys

    def get_num_of_keys(self):
        return self.num_of_keys


class KSA:
    def __init__(self, m: int):
        self.S = np.arange(m)

    def _get_m(self):
        return self.S.shape[0]

    @property
    def m(self):
        return self.S.shape[0]

    def get(self):
        return self.S

    def schedule(self, keys: Keys):
        assert keys.get_num_of_keys() <= self.m
        j = 0
        l = keys.get_num_of_keys()
        for i in range(self.m):
            j = (j + self.S[i] + keys.keys[i % l]) % self.m
            self.S[i], self.S[j] = self.S[j], self.S[i]


if __name__ == "__main__":
    keys = Keys(np.array([3, 4, 7]))
    ksa = KSA(m=10)
    ksa.schedule(keys)
    print(ksa.S)
