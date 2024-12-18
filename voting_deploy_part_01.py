import json
from web3 import Web3
from solcx import compile_standard, install_solc

with open("./Election.sol", "r") as file:
    election_list_file = file.read()

# Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"Election.sol": {"content": election_list_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled_code_election.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["Election.sol"]["Election"]["evm"]["bytecode"]["object"]

# get abi
abi = json.loads(compiled_sol["contracts"]["Election.sol"]["Election"]["metadata"])["output"]["abi"]


# For connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337

# this is the ganache-cli public and private key
my_address = "0x6f65a6387eF8fEF2AF0edBCc6B374d970Ec135E5"
private_key = "0x055d740544c9d390a340c37e25a98e65485f4200ed9d10806c82b6d898a5609d"
