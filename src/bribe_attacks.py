"""
In hybrid systems, especially during transitions, bribing validators to favor one chain over another can be a significant risk. This might involve financial incentives outside the blockchain system.
"""

from block import Block
from blockchain import Blockchain

def bribe_attack(blockchain, bribe_transactions):
    """
    Perform a bribe attack by creating a block with bribed transactions.

    Parameters
    ----------
    blockchain : Blockchain

    bribe_transactions : str
        Transactions for the bribed block

    Returns
    -------
    Block
        A bribed block
    """
    # Attacker bribes validators to prioritize specific transactions
    last_block = blockchain.get_last_block()

    # Bribed block with the bribed transactions
    bribed_block = Block(index=last_block.index + 1, transactions=bribe_transactions, previous_hash=last_block.hash)
    
    # Mine the block
    bribed_block.mine_block(blockchain.difficulty)
    
    return bribed_block

blockchain = Blockchain()
blockchain.add_node("node1")
blockchain.add_to_stake("node1", 100)  # node1 stakes 100

# Mining a new block
new_block = Block(index=1, transactions="Tx1", previous_hash=blockchain.get_last_block().hash)
blockchain.add_block(new_block)

# Demonstrating a bribe to prioritize specific transactions
bribed_block = bribe_attack(blockchain, "Bribed Tx")
print("Bribed Block Hash:", bribed_block.hash)
