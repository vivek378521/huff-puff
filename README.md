# Huffman Coding Python Package

This Python package implements Huffman coding for file compression and decompression.

## Installation

You can install the package using pip:

```bash
pip install huff-puff
```

## Usage

### Compression (huff.py)

To compress a file using Huffman coding:

```python
from huff import compress

compressedFile = compress("input.txt")
```

### Decompression (huff.py)

To decompress a file previously compressed using Huffman coding:

```python
from huff import decompress

decompressedFile = decompress("input_compressed.bin")
```

### Huffman Functions (huffman.py)

For detailed information about the Huffman coding functions:

```python
from huffman import make_frequency_dict, make_heap, merge_nodes, make_codes, get_encoded_text, decode_text
// Use these functions as needed within your code
```

## License

This project is licensed under the [MIT License](LICENSE).