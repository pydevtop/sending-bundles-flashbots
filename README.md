# Flashbots Transaction Sender
Sending flashbot bundles to python

<p align="center"><img width="1024" src="https://py-dev.top/images/sending_bundles_flashbots/sending-bundles-flashbots.webp"></p>

This repository provides a Python script for sending transactions via Flashbots to bypass the public mempool and avoid frontrunning. The script utilizes Web3.py and the Flashbots API to submit bundles directly to miners

## Features
Web3 Integration: Connects to Ethereum using an Infura RPC
Flashbots Compatibility: Uses Flashbots for transaction bundling
Dynamic Gas Adjustments: Adjusts gas fees automatically to increase transaction success rate
Mempool Monitoring: Checks whether a transaction has been included
Automated Retries: Increases gas fees progressively in case of failures

## Installation

1. Clone the repository:
```
git clone https://github.com/pydevtop/sending-bundles-flashbots.git
cd sending-bundles-flashbots
``` 

###  Create a virtual environment venv:

```
python -m venv venv
```

###  Activate the environment:

```
c:\sending-bundles-flashbots\venv\Scripts\activate
```

## Install dependencies:

```
pip install -r requirements.txt  

```

## Configuration
Set your Ethereum RPC, private key, and recipient wallet in config.py or directly in the script:

```
RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
SEND_WALLET = "0xRecipientAddress"

```

## Usage
Run the script to send transactions via Flashbots:

```
python main.py  

```
## Result
```
Connected to Ethereum network: Geth/v1.14.13-stable-eb00f169/linux-amd64/go1.23.5
Account address: 0xC3f78F263c6862EFfE82C887DB6C872cb9A64E46
Base Fee: 565751357
Initial Priority Fee: 57704721
Max Fee Per Gas: 680031213
Sending bundle to block 7712502...
Bundle: [{'signed_transaction': HexBytes('0x02f87783aa36a782059083580ce884288873ed83061a80941255a27b98c04dd2ec429908e0d03351c6af9c8e88016345785d8a000080c080a0f8c2d6da5c68c478012c728f82288ad7d90991d60c0e837d251bf8e2c3e14f85a02d93ed1ae3c2bebc956b80484ce05fb8aaa68a98ce3180ffda174c04b0aad7f3')}]
Transaction sent via Flashbots to block 7712502, waiting...
Transaction confirmed in block 7712502.
TX Hash: 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (1/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (2/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (3/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (4/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (5/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (6/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (7/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (8/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (9/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e not in mempool. Retrying... (10/10)
Transaction 0x09f56bf472ba580a7231b2dcb5b87c8d529cd495b3af710c9e6673089fd8777e is still missing. Increasing gas fees...
New Max Fee Per Gas: 1020046819, New Priority Fee: 63475193
Sending bundle to block 7712504...
Bundle: [{'signed_transaction': HexBytes('0x02f87783aa36a782059083580ce8843cccade383061a80941255a27b98c04dd2ec429908e0d03351c6af9c8e88016345785d8a000080c080a06eaff177a699ebdcc2c9b6ce1daeea37e8dc32e99bd39f929abdbb37d7d1fc29a07e5bfc3785636e6f54f39492a7238a97dbfe8d8085edd94828b7a6084bd0cb0a')}]
Transaction sent via Flashbots to block 7712504, waiting...
Transaction confirmed in block 7712504.
TX Hash: 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (1/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (2/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (3/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (4/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (5/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (6/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (7/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (8/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (9/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa not in mempool. Retrying... (10/10)
Transaction 0x64cd7616bd0447b8f20a6c6e1b75cb400ea4603ed269c8acf879ba58f2165faa is still missing. Increasing gas fees...
New Max Fee Per Gas: 1530070228, New Priority Fee: 69245665
Sending bundle to block 7712507...
Bundle: [{'signed_transaction': HexBytes('0x02f87783aa36a782059083580ce8845b3304d483061a80941255a27b98c04dd2ec429908e0d03351c6af9c8e88016345785d8a000080c001a03847b85bf9004ee7a819b303b7af99fb72488ce7dffa006e02dcdf9f836eb6f1a005a603426f05ed8f7c2fb4e4e61065d01ee8f3fe5addb2c882be4db15d40c89f')}]
Transaction sent via Flashbots to block 7712507, waiting...
Transaction confirmed in block 7712507.
TX Hash: 0xa34e58b5fd9207a6ff7d40fd2d8af61f1b74dc35b9ff212fee6cb02aac96e5a0
Transaction 0xa34e58b5fd9207a6ff7d40fd2d8af61f1b74dc35b9ff212fee6cb02aac96e5a0 is in mempool!  

```


## Dependencies:
### web3
### eth-account
### flashbots

### License MIT


## Contacts
Telegram:  @morgan_sql<br>
Telegram channel: https://t.me/pydevtop

## License and Usage Notice

This project is licensed under the MIT License.

⚠️ However, unauthorized copying, redistribution, publication, or forking of this repository in a way that falsely attributes authorship or contributor status is strictly prohibited.

The author (PyDev) does not consent to being listed as a contributor in unauthorized forks or copies of this repository.

If you find any unauthorized fork or copy that misuses the author’s name, please report it to GitHub Support.

Author: PyDev

