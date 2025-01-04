import json
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.rpc.core import Transaction
from solana.system_program import CreateAccountParams, create_account
from solana.keypair import Keypair

class SynthFramework:
    def __init__(self, cluster_url='https://api.mainnet-beta.solana.com'):
        self.client = Client(cluster_url)

    def get_account_info(self, public_key):
        response = self.client.get_account_info(PublicKey(public_key))
        if not response['result']['value']:
            raise Exception('Account not found')
        return response['result']

    def create_account(self, payer_keypair_path, space=0, program_id=PublicKey("11111111111111111111111111111111")):
        with open(payer_keypair_path, 'r') as f:
            payer_keypair = Keypair.from_secret_key(json.load(f))
        
        new_account = Keypair.generate()
        lamports = self.client.get_minimum_balance_for_rent_exemption(space)['result']

        tx = Transaction()
        tx.add(create_account(CreateAccountParams(
            from_pubkey=payer_keypair.public_key,
            new_account_pubkey=new_account.public_key,
            lamports=lamports,
            space=space,
            program_id=program_id
        )))

        response = self.client.send_transaction(tx, payer_keypair)
        return response
