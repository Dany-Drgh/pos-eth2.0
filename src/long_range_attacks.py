"""
Long-range attacks involve an attacker acquiring old private keys from former stakeholders to create an alternative chain from a point far back in the blockchain’s history. This can be a threat particularly in PoS, as historical keys might still be effective.
"""

from block import Block
from blockchain import Blockchain

def long_range_attack(blockchain, old_index, malicious_transactions):
    """
    Perform a long-range attack by creating a malicious block from an old block.

    Parameters
    ----------
    blockchain : Blockchain
        A blockchain instance
    old_index : int
        Index of the old block to use
    malicious_transactions : str
        Transactions for the malicious block

    Returns
    -------
    Block
        A malicious block
    """
    # Attacker uses an old block to start a new chain
    old_block = blockchain.chain[old_index]
    malicious_block = Block(index=old_block.index + 1, transactions=malicious_transactions, previous_hash=old_block.hash)
    malicious_block.mine_block(blockchain.difficulty)
    return malicious_block

blockchain = Blockchain()
blockchain.add_node("node1")
blockchain.add_to_stake("node1", 100)  # node1 stakes 100

# Mining a new block
new_block = Block(index=1, transactions="Tx1", previous_hash=blockchain.get_last_block().hash)
blockchain.add_block(new_block)

# Assuming the attacker has access to the blockchain at block index 1
malicious_block = long_range_attack(blockchain, 1, "Malicious Tx")
print("Malicious Block Hash:", malicious_block.hash)
