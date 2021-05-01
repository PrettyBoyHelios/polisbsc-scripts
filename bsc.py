import json
import os.path

from web3 import Web3


class RPCNode:
    def __init__(self, node, dao):
        self.rpc = Web3(Web3.HTTPProvider(node))
        with open(os.path.join("abi", "plutus.json")) as file:
            data = json.load(file)
            self.polis_staking_contract_abi = data['abi']
            self.polis_staking_contract_address = data['contract']
        with open(os.path.join("abi", "validator.json")) as file:
            data = json.load(file)
            self.polis_validator_contract_abi = data['abi']
            self.polis_validator_contract_address = data['contract']
        self.polis_staking_contract = self.rpc.eth.contract(self.polis_staking_contract_address, abi=self.polis_staking_contract_abi)
        self.polis_validator_contract = self.rpc.eth.contract(self.polis_validator_contract_address,
                                                            abi=self.polis_validator_contract_abi)
        self.dao_address = Web3.toChecksumAddress(dao)

    def get_staking_reward(self):
        pending_polis = self.polis_staking_contract.functions.pendingPolis(0, self.dao_address).call()
        print("Pending Polis to Claim: {} POLIS".format(pending_polis/1e18))

    def get_delegated_votes(self, address: str) -> float:
        """
        Returns the amount of delegated votes to an address at the latest block.
        :param address: address used to query the total amount of delegated votes.
        :return: the amount of votes delegated to a given address.
        """
        votes = self.polis_validator_contract.functions.getCurrentVotes(address).call()
        return votes/1e18
