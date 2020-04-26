import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "{}{}".format(self.timestamp, self.data).encode()
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None

    def create_new_block(self, data, last_block):
        if last_block is not None:
            previous_hash = last_block.hash
        else:
            previous_hash = None

        block = Block(
            timestamp=time.strftime("%H:%M %d/%m/%Y", time.gmtime()),
            data=data,
            previous_hash=previous_hash
        )
        block.hash = block.calc_hash()
        return block

    def add_to_chain(self, block):
        if self.head is None:
            self.head = block
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = block


# Test cases
blockchain = BlockChain()
block1 = blockchain.create_new_block("abc", None)
block2 = blockchain.create_new_block("def", block1)
block3 = blockchain.create_new_block("123", block2)
block4 = blockchain.create_new_block("123", block3)

blockchain.add_to_chain(block1)
blockchain.add_to_chain(block2)
blockchain.add_to_chain(block4)
blockchain.add_to_chain(block3)

node = blockchain.head
while node:
    print("timestamp: ", node.timestamp)
    print("data: ", node.data)
    print("previous_hash: ", node.previous_hash)
    print("hash:", node.hash)
    print("------------------------------------------------------------------")
    node = node.next
