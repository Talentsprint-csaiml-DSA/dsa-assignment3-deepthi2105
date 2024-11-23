import heapq
from collections import Counter

# Node structure for the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison operators for priority queue
    def __lt__(self, other):
        # Ensure consistent tie-breaking by comparing characters lexicographically
        if self.freq == other.freq:
            return (self.char or '') < (other.char or '')
        return self.freq < other.freq

# Generate Huffman Codes
def generate_codes(root, current_code, codes):
    if root is None:
        return

    # If this is a leaf node, store the code
    if root.char is not None:
        codes[root.char] = current_code
        return

    # Traverse left and right subtrees
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

# Huffman Coding function
def huffman_coding(text):
    # Step 1: Count character frequencies
    frequency = Counter(text)

    # Step 2: Build the priority queue (min-heap)
    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    # Step 3: Build the Huffman Tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)  # Smallest frequency
        node2 = heapq.heappop(heap)  # Second smallest frequency

        # Merge the two nodes
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    # The root of the tree
    root = heap[0]

    # Step 4: Generate the codes
    codes = {}
    generate_codes(root, "", codes)

    # Step 5: Encode the text
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text

