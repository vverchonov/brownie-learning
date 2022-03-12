from brownie import accounts, Storage


def readLastContract():
    contract = Storage[-1]
    print(contract.showNumber())


def main():
    readLastContract()
