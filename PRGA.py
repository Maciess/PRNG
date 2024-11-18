from KSA import KSA, Keys
import numpy as np


class PRGA:
    def __init__(self, permutation: KSA):
        self.key = permutation

    def get_random(self, size: int = 1):
        i = 0
        j = 0
        random_result = np.empty(size, dtype=int)
        for index in range(size):
            i = (i + 1) % self.key.m
            j = (j + self.key.get()[i]) % self.key.m
            self.key.get()[i], self.key.get()[j] = self.key.get()[j], self.key.get()[i]
            t = (self.key.get()[i] + self.key.get()[j]) % self.key.m
            random_result[index] = self.key.get()[t]
        return random_result


if __name__ == "__main__":
        keys = Keys(np.array([3, 4, 2, 5]))
        ksa = KSA(m=10)
        ksa.schedule(keys)
        prga = PRGA(ksa)
        print(prga.get_random(30))
