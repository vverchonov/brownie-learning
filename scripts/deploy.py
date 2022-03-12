from brownie import accounts, Storage
import os


def deployStorage():
    account = accounts[0]
    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)
    storage = Storage.deploy({"from": account})
    print(storage.showNumber())
    trs = storage.store(5, {"from": account})
    trs.wait(1)
    print(storage.showNumber())


def main():
    deployStorage()
