import base64
import requests
import json


def get_transactions_from_block(block_height: int) -> list[bytes]:
    response = requests.get(f'https://rpc.akashnet.net/block?height={block_height}')
    json_data = json.loads(response.text)

    transactions_data_b64 = []
    try:
        transactions_data_b64 = json_data['result']['block']['data']['txs']
    except KeyError:
        pass

    if transactions_data_b64:
        decoded_transactions = [
            base64.b64decode(encoded_transaction) for encoded_transaction in transactions_data_b64
        ]
        return decoded_transactions

    return []


print(get_transactions_from_block(12601044))
