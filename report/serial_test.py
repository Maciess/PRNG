import numpy as np
from scipy.stats import chi

def split_hypercube(m, L):
    """
    Split the hypercube [0,1]^m into L^m smaller equal cubes.

    Parameters:
        m (int): Number of dimensions of the hypercube.
        L (int): Number of divisions per dimension.

    Returns:
        list: A list of numpy arrays, each representing a smaller cube.
    """
    # Generate division points for each dimension
    points = np.linspace(0, 1, L + 1)  # L+1 points including 0 and 1
    # Generate all combinations of lower bounds
    grids = np.meshgrid(*([points[:-1]] * m), indexing='ij')
    lower_bounds = np.array([grid.ravel() for grid in grids]).T  # Shape: (L^m, m)
    # Calculate upper bounds by adding 1/L to each lower bound
    upper_bounds = lower_bounds + 1 / L
    # Create cubes in the desired representation
    cubes = [np.stack([lower, upper], axis=1) for lower, upper in zip(lower_bounds, upper_bounds)]
    return cubes


def convert_cube_to_bounds(cube):
    lower_bounds = cube[:, 0]  # Lower bounds for each dimension
    upper_bounds = cube[:, 1]
    return (lower_bounds, upper_bounds)


def is_within_hypercube(vector, cube):
    lower_bounds, upper_bounds = convert_cube_to_bounds(cube)
    # Check if the vector is within bounds for all dimensions
    # we don't care about bounds here
    return np.all(vector >= lower_bounds) and np.all(vector <= upper_bounds)


def serial_test(sample, m, l):
    assert len(sample) % m == 0, "Sample size must be length n=m*r"
    cube_collection = split_hypercube(m, l)  # should return l^m cubes
    sample_divided = np.split(sample, range(m, len(sample), m))  # divide sample into m vectors
    r = len(sample_divided)
    k = l ** m
    assert k == len(cube_collection), "Incorrect cube collection size"
    cube_counts = np.zeros(k, dtype=np.uint16)
    for m_dim_vector in sample_divided:  # arrow code :(
        for cube_index, cube in enumerate(cube_collection):
            is_in_cube = is_within_hypercube(m_dim_vector, cube)
            cube_counts[cube_index] += is_in_cube
    expected_mean = r / k
    assert np.sum(cube_counts) == r, "Incorrect cube counts probably at least one point belong to two buckets"
    stat = np.sum(((cube_counts - expected_mean) ** 2)) / expected_mean
    p_value = 1 - chi.cdf(stat, df=k - 1)

    return (stat, p_value)


if __name__ == "__main__":
    print(serial_test(np.random.random(3 * 100000), m=3, l=2))
