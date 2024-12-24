import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash, timestamp=None):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        assert self.hash is not None, "The hash must be calculated before mining."
        pattern = '0' * difficulty # difficulty is the number of leading zeros that must be in the hash
        while not self.hash.startswith(pattern):
            self.nonce += 1
            self.hash = self.calculate_hash()
