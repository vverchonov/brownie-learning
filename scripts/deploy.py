from brownie import accounts, Storage, network
import os


def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(os.getenv("PRIVATE_KEY"))


def deployStorage():
    account = getAccount()
    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)
    storage = Storage.deploy({"from": account})
    print(storage.showNumber())
    trs = storage.store(5, {"from": account})
    trs.wait(1)
    print(storage.showNumber())


def main():
    deployStorage()
