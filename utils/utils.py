import os.path
import pandas as pd
from typing import List


def load_holders() -> List[str]:
    """
    Loads Polis Holder data from data/holders.csv and returns a list with all the addresses.
    :return: List with all Polis holders addresses (up to 100,000 addresses).
    """
    holders = pd.read_csv(os.path.join("data", "holders.csv"))
    holder_array = list()
    for holder in holders['HolderAddress']:
        holder_array.append(holder)
    print(holder_array)
    return holder_array
