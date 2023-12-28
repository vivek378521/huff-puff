import unittest
import os
from huff import compress, decompress


class TestHuffmanEncodingDecoding(unittest.TestCase):
    def setUp(self):
        self.test_text = "hello world"
        self.original_file = "test_file.txt"

        # Create the original file with test text
        with open(self.original_file, "w") as file:
            file.write(self.test_text)

    def test_compress_decompress(self):
        compressed_file = compress(self.original_file)
        decompressed_file = decompress(compressed_file)

        with open(self.original_file, "r") as original, open(
            decompressed_file, "r"
        ) as decompressed:
            original_text = original.read()
            decompressed_text = decompressed.read()

            self.assertEqual(
                original_text,
                decompressed_text,
                "Decompressed text does not match original text.",
            )

    def tearDown(self):
        # Clean up files created during testing
        test_files = [
            self.original_file,
            "test_file_compressed.bin",
            "test_file_decompressed.txt",
            "test_file_compressed_decompressed.txt",
        ]
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)


if __name__ == "__main__":
    unittest.main()
