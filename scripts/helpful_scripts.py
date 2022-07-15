from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")
        #We only need to deploy the MockV3Aggregator to the network once
        if len(MockV3Aggregator) <= 0:
        #Web3.toWei() Returns the value in the denomination specified by the currency argument "ether" converted to wei.
        #ETH to Wei exactly adds the desired amount of 0's to $2000
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mocks Deployed!")