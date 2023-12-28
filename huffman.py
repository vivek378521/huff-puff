import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def make_frequency_dict(text):
    frequency = {}
    for character in text:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1
    return frequency


def make_heap(frequency):
    heap = []
    for key in frequency:
        node = HeapNode(key, frequency[key])
        heapq.heappush(heap, node)
    return heap


def merge_nodes(heap):
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = HeapNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)


def make_codes_helper(root, current_code, codes, reverse_mapping):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        reverse_mapping[current_code] = root.char
        return

    make_codes_helper(root.left, current_code + "0", codes, reverse_mapping)
    make_codes_helper(root.right, current_code + "1", codes, reverse_mapping)


def make_codes(root):
    codes = {}
    reverse_mapping = {}
    make_codes_helper(root, "", codes, reverse_mapping)
    return codes, reverse_mapping


def get_encoded_text(text, codes):
    encoded_text = ""
    for character in text:
        encoded_text += codes[character]
    return encoded_text
