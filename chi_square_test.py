import numpy as np

default_partition = np.array([0.2, 0.4, 0.6, 0.8])


def get_bin(num, partition=default_partition):
    for index, bin in enumerate(partition):
        if num > bin:
            continue
        else:
            return index
    return partition.shape[0]


def calculate_partition_probabilities(default_partition):
    """
    Calculate the probability of each partition.

    Parameters:
        default_partition (np.ndarray): Array defining the partition endpoints.

    Returns:
        dict: Dictionary of partitions with their corresponding probabilities.
    """
    # Sort the default partition and include 0 and 1 for completeness
    sorted_partition = np.sort(np.unique(np.concatenate(([0], default_partition, [1]))))
    partitions = [(sorted_partition[i], sorted_partition[i + 1]) for i in range(len(sorted_partition) - 1)]
    probabilities = np.diff(sorted_partition)
    return probabilities


def chi_square_test(random_vector, partition=default_partition):
    """
    :param random_vector: array of random numbers from 0,1, parition
    :return: p-value, real value from [0,1].
    """
    r = random_vector.size
    category_counts = np.array([get_bin(x, partition) for x in random_vector])
    category_counts = np.bincount(category_counts)
    category_prob = calculate_partition_probabilities(partition)
    statistics = np.sum(((category_counts - r * category_prob) ** 2) / r * category_prob)
    return statistics


if __name__ == "__main__":
    sample = np.random.rand(1000)
    stat = chi_square_test(sample)
    print(stat)
