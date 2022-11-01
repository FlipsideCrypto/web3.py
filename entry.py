import json

from web3 import EthereumTesterProvider
from web3.main import Web3
from web3.contract import decode_abi

w3 = Web3(None)

with open ('tether.json') as f:
    tether = json.load(f)
contract_address = '0xdac17f958d2ee523a2206206994597c13d831ec7'
myContract = w3.eth.contract(address=contract_address, abi=tether)
