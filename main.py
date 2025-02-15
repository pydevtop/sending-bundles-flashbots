import time
from web3 import Web3
from eth_account import Account
from flashbots import flashbot, Flashbots
from web3.exceptions import TransactionNotFound



def is_tx_in_mempool(web3, tx_hash):
    """ Checks if there is a transaction in the mempool """
    try:
        web3.eth.get_transaction(tx_hash)
        return True
    except TransactionNotFound:
        return False

def check_flashbots(web3, private_key, send_wallet):
    try:
        if not web3.is_connected():
            print("Web3 is not connected. Check your RPC URL.")
            return

        print(f"Connected to Ethereum network: {web3.client_version}")

        account = Account.from_key(private_key)
        print(f"Account address: {account.address}")

        flashbot(web3, account)

        latest_block = web3.eth.get_block('latest')
        base_fee = latest_block.get('baseFeePerGas', 0)

        priority_fee_per_gas = int(web3.eth.gas_price * 0.1)  # Priority commission assessment (10% of current gas_price)
        max_fee_per_gas = int(base_fee * 1.1) + priority_fee_per_gas  # Minimum 10% more than base_fee

        print(f"Base Fee: {base_fee}")
        print(f"Initial Priority Fee: {priority_fee_per_gas}")
        print(f"Max Fee Per Gas: {max_fee_per_gas}")

        max_retries = 10
        priority_fee_increment = int(priority_fee_per_gas *  0.1)  # Increase by 10% on each failure

        while True:
            for i in range(max_retries):

                target_block = web3.eth.block_number + 1
                print(f"Sending bundle to block {target_block}...")

                # Increase max_fee_per_gas if it is less than base_fee
                if max_fee_per_gas < base_fee:
                    print(f"Adjusting maxFeePerGas: {max_fee_per_gas} -> {base_fee * 1.2}")

                    max_fee_per_gas = int(base_fee * 1.2)

                tx = {
                    "to": send_wallet,
                    "value": web3.to_wei(0.1, "ether"),
                    "gas": 400000,
                    'maxPriorityFeePerGas': priority_fee_increment,
                    'maxFeePerGas': max_fee_per_gas,
                    "nonce": web3.eth.get_transaction_count(account.address),
                    "chainId": web3.eth.chain_id,
                }


                signed_tx = account.sign_transaction(tx)
                bundle = [{"signed_transaction": signed_tx.rawTransaction}]
                print(f"Bundle: {bundle}")

                flashbots = Flashbots(web3)

                try:
                    flashbots.simulate(bundle, target_block)
                    send_result = flashbots.send_bundle(bundle, target_block)
                    print(f"Transaction sent via Flashbots to block {target_block}, waiting...")

                    send_result.wait()
                    print(f"Transaction confirmed in block {target_block}.")

                    tx_hash = signed_tx.hash.hex()
                    print(f"TX Hash: {tx_hash}")

                    retries = 0
                    while not is_tx_in_mempool(web3, tx_hash) and retries < max_retries:
                        print(f"Transaction {tx_hash} not in mempool. Retrying... ({retries + 1}/{max_retries})")
                        time.sleep(2)
                        retries += 1

                    if is_tx_in_mempool(web3, tx_hash):
                        print(f"Transaction {tx_hash} is in mempool!")
                        return

                    print(f"Transaction {tx_hash} is still missing. Increasing gas fees...")

                    priority_fee_per_gas += priority_fee_increment  # Increasing the priority commission
                    max_fee_per_gas = int(max_fee_per_gas * 1.5)  # Increase maxFeePerGas by 50%

                    print(f"New Max Fee Per Gas: {max_fee_per_gas}, New Priority Fee: {priority_fee_per_gas}")

                    break


                except Exception as send_error:
                    print(f"Error while sending transaction: {send_error}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
    PRIVATE_KEY = "YOUR_PRIVATE_KEY"
    SEND_WALLET = "0xRecipientAddress"
    web3 = Web3(Web3.HTTPProvider(RPC_URL))
    check_flashbots(web3, PRIVATE_KEY, SEND_WALLET)

