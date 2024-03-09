from .utils.time import timeit
import numpy as np
from pathlib import Path

N = 100_000
# set a random seed
np.random.seed(42)

# define the data folder
data_folder = Path(__file__).parent / "data"


@timeit
def faker():
    # print cwd
    import os

    print("Current working directory:", os.getcwd())
    with open(data_folder / "countries.txt") as f:
        csv = f.read().splitlines()

    x = np.array(csv)

    np.random.choice(x, N, replace=True)


faker()
