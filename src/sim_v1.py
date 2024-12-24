from block import Block
from blockchain import Blockchain



blockchain = Blockchain()
blockchain.add_node("node1")
blockchain.add_to_stake("node1", 100)  # node1 stakes 100

# Mining a new block
new_block = Block(index=1, transactions="Tx1", previous_hash=blockchain.get_last_block().hash)
blockchain.add_block(new_block)

print(f"Blockchain is valid: {blockchain.is_valid()}")
print(f"Latest block has hash: {blockchain.get_last_block().hash}")
