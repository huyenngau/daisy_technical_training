import heapq
import sys
from collections import defaultdict


class HeapNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    # Compare 2 HeapNode by frequency
    def __lt__(self, other):
        if not isinstance(other, HeapNode):
            raise TypeError(f"'<' not supported between instances of {type(self)} and {type(other)}")
        return self.frequency < other.frequency


class Huffman:
    # Build a tree
    # Merge 2 minimum nodes in Heap until the heap contains only one node
    def build_a_huffman_tree(self, input_str):
        # Make char_frequency dict
        frequencies = defaultdict(int)
        for char in input_str:
            frequencies[char] += 1

        # Add items in frequencies into Heap
        heap = []
        for char, frequency in frequencies.items():
            node = HeapNode(char, frequency)
            heapq.heappush(heap, node)  # Push the value item onto the heap, maintaining the heap invariant

        while len(heap) > 1:
            # Get 2 minimum nodes from Heap
            # Using heappop to pop and return the smallest item from the heap, maintaining the heap invariant
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)

            # Create a new internal node with a frequencies equal to the sum of the two nodes frequencies
            merged_node = HeapNode(None, node1.frequency + node2.frequency)
            # Make the first extracted node as its left child and the other extracted node as its right child
            merged_node.left = node1
            merged_node.right = node2

            # Add this node to the min heap
            heapq.heappush(heap, merged_node)

        huffman_tree = heapq.heappop(heap)
        # remove the frequencies from the previously built tree
        self.trim_huffman_tree(huffman_tree)
        return huffman_tree

    def trim_huffman_tree(self, tree):
        tree.frequency = None
        if tree.left:
            self.trim_huffman_tree(tree.left)
        if tree.right:
            self.trim_huffman_tree(tree.right)

    def make_binary_code(self, root, current_code, codes):
        if root is None:
            return

        # Find until root node has "char" is None
        if root.char is not None:
            codes[root.char] = current_code

        self.make_binary_code(root.left, current_code + "0", codes)
        self.make_binary_code(root.right, current_code + "1", codes)
        return codes

    def get_encoded_data(self, input_str):
        huffman_tree = self.build_a_huffman_tree(input_str)

        codes = self.make_binary_code(huffman_tree, "", {})
        encoded_data = ""

        for character in input_str:
            encoded_data += codes[character]
        return encoded_data, huffman_tree

    def get_decoded_data(self, encoded_data, huffman_tree):
        decoded_data = ""
        # start from root and do following until a leaf is found
        current_node = huffman_tree
        for bit in encoded_data:
            # If current bit is 0, move to left node of the tree
            if bit == "0":
                current_node = current_node.left
            # If the bit is 1, move to right node of the tree
            else:
                current_node = current_node.right

            # If during traversal, encounter a leaf node, print character of that particular leaf node
            if current_node.left is None and current_node.right is None:
                decoded_data += current_node.char
                # then again continue the iteration of the encoded data starting from step 1
                current_node = huffman_tree

        return decoded_data


def huffman_encoding(data):
    huffman = Huffman()
    return huffman.get_encoded_data(data)


def huffman_decoding(encoded_data, tree):
    huffman = Huffman()
    return huffman.get_decoded_data(encoded_data, tree)


def test_function(input_str):
    print("The size of the data is: {}\n".format(sys.getsizeof(input_str)))
    print("The content of the data is: {}\n".format(input_str))
    encoded_data, tree = huffman_encoding(input_str)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


# Test cases
string_1 = "Hello"
test_function(string_1)
print("--------------------------------------------------------------------------")

string_2 = "The bird is the word"
test_function(string_2)
print("--------------------------------------------------------------------------")

string_3 = "abc"
test_function(string_3)
print("--------------------------------------------------------------------------")
