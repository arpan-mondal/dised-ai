from algosdk import algod, transaction
from algosdk.future.transaction import ApplicationCallTxn
from algosdk.v2client import algod
from algosdk import kmd
from algosdk.error import AlgodHTTPError

# Initialize the Algorand client
algod_address = "http://localhost:4001"  # Replace with your node address
algod_token = "your-node-token"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Your smart contract and user accounts
contract_account = "your-contract-address"
user_address = "user-address"
user_private_key = "user-private-key"

# Tokenize AI API
def tokenize_api(api_name, price):
    params = algod_client.suggested_params()
    unsigned_txn = ApplicationCallTxn(
        sender=user_address,
        sp=params,
        index=contract_account,
        app_on_complete=transaction.OnComplete.NoOpOC,
        app_id=123,  # Replace with your app ID
        app_args=[api_name.encode("utf-8"), str(price).encode("utf-8")]
    )
    signed_txn = unsigned_txn.sign(user_private_key)

    try:
        tx_id = algod_client.send_transaction(signed_txn)
        print(f"Tokenization transaction ID: {tx_id}")
    except AlgodHTTPError as e:
        print(e)

# Purchase AI API
def purchase_api(api_name, price):
    params = algod_client.suggested_params()
    unsigned_txn = ApplicationCallTxn(
        sender=user_address,
        sp=params,
        index=contract_account,
        app_on_complete=transaction.OnComplete.NoOpOC,
        app_id=123,  # Replace with your app ID
        app_args=[api_name.encode("utf-8", str(price).encode("utf-8")]
    )
    signed_txn = unsigned_txn.sign(user_private_key)

    try:
        tx_id = algod_client.send_transaction(signed_txn)
        print(f"Purchase transaction ID: {tx_id}")
    except AlgodHTTPError as e:
        print(e)

# Example usage:
# Tokenize an AI API with a price of 10 ALGO
tokenize_api("AI_API_1", 10)

# Purchase an AI API
purchase_api("AI_API_1", 10)
