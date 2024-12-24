"""
In PoS, the "nothing at stake" problem arises because validators might want to vote on multiple blockchain histories to maximize their chances of receiving transaction fees. This is more likely to occur during the PoW to PoS transition phase or in any hybrid setup where older rules might still apply.

Simulating the Issue
You could simulate this by having a validator create blocks on different forks.
"""

from block import Block
from blockchain import Blockchain

def simulate_nothing_at_stake(blockchain):

    """
    Simulate the "nothing at stake" problem by creating blocks on different forks.

    Parameters
    ----------
    blockchain : Blockchain
        A blockchain instance

    Returns
    -------
    tuple
        A tuple of two blocks on different forks
    """


    # Simulate creating blocks on different forks
    original_block = blockchain.get_last_block()

    # Validator creates a fork by referencing an older block
    fork_block = Block(index=original_block.index + 1, transactions="Tx on Fork", previous_hash=original_block.previous_hash)
    fork_block.mine_block(blockchain.difficulty)

    # Validator also mines on the main chain
    main_chain_block = Block(index=original_block.index + 1, transactions="Tx on Main Chain", previous_hash=original_block.hash)
    main_chain_block.mine_block(blockchain.difficulty)

    return fork_block, main_chain_block

blockchain = Blockchain()
blockchain.add_node("node1")
blockchain.add_to_stake("node1", 100)  # node1 stakes 100

# Mining a new block
new_block = Block(index=1, transactions="Tx1", previous_hash=blockchain.get_last_block().hash)
blockchain.add_block(new_block)

fork_block, main_chain_block = simulate_nothing_at_stake(blockchain)
print("Fork Block Hash:", fork_block.hash)
print("Main Chain Block Hash:", main_chain_block.hash)
