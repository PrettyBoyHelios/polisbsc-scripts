from web3 import Web3
from bsc import RPCNode
from utils.utils import load_holders

if __name__ == '__main__':
    rpc_node = RPCNode("https://bsc-dataseed2.defibit.io/", "0xEd971DCa3D893aAA254606Ee77883070A8ddBb32")
    # rpc_node.get_staking_reward()
    holders = load_holders()
    delegated_power = 0
    for address in holders:
        power = rpc_node.get_delegated_votes(Web3.toChecksumAddress(address))
        if power > 0:
            print("{}, {}".format(address, power))
        delegated_power += power
    print("\nTotal Delegated Power: ", delegated_power)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
