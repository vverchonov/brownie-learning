from brownie import Storage, accounts
import os


def testDeploy():
    # Arrange
    account = accounts[0]
    # Act
    storage = Storage.deploy({"from": account})
    value_start = storage.showNumber()
    expected = 0
    # Assert
    assert value_start == expected


def testUpdate():
    account = accounts[0]
    storage = Storage.deploy({"from": account})
    storage.store(10, {"from": account})
    expected = 10
    assert storage.showNumber() == expected

    # -pdb -check during compile
    # -k check single
    # -s print + each test passed or no
