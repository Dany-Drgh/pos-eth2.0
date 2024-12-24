from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()] # create the genesis block
        self.difficulty = 2 # set the difficulty level
        self.nodes = set() # this will store the nodes in the network
        self.stakes = {}  # this will track the balance to simulate staking

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if (current.hash != current.calculate_hash() or
                current.previous_hash != previous.hash):
                return False

        return True

    def add_node(self, address):
        self.nodes.add(address)

    def add_to_stake(self, node_address, amount):
        if node_address in self.stakes:
            self.stakes[node_address] += amount
        else:
            self.stakes[node_address] = amount

    def proof_of_stake(self):
        # This is a very simplified version of PoS
        total_stakes = sum(self.stakes.values()) # total amount of stakes
        winner_node = None 
        max_stake = 0

        for node, stake in self.stakes.items():
            if stake > max_stake and stake / total_stakes > 0.01:  # minimum 1% stake to be eligible
                # the node with the highest stake is the winner
                winner_node = node  
                max_stake = stake

        return winner_node
