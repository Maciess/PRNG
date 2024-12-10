import math
from scipy.stats import norm

def frequency_monobit_test(bits):
    n = len(bits)
    S = sum(1 if bit == '1' else -1 for bit in bits)
    S_obs = abs(S) / math.sqrt(n)
    p_value = 2 * (1 - norm.cdf(S_obs))
    return p_value

# Example binary sequence
binary_sequence = '11001010111101010101'
p_value = frequency_monobit_test(binary_sequence)
if p_value >= 0.01:
    print("The sequence passes the Frequency (Monobit) Test (p-value: {:.5f})".format(p_value))
else:
    print("The sequence fails the Frequency (Monobit) Test (p-value: {:.5f})".format(p_value))
