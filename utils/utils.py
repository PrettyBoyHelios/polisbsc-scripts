import os.path
import pandas as pd


def load_holders():
    holders = pd.read_csv(os.path.join("data", "holders.csv"))
    holder_array = list()
    for holder in holders['HolderAddress']:
        holder_array.append(holder)
    print(holder_array)
    return holder_array
