import os
import argparse
import pickle

from huffman import (
    make_frequency_dict,
    make_heap,
    merge_nodes,
    make_codes,
    get_encoded_text,
)


def decompress(file_path):
    filename, file_extension = os.path.splitext(file_path)
    output_path = filename + "_decompressed.txt"

    with open(file_path, "rb") as file:
        frequency = pickle.load(file)  # Load frequency dictionary from header
        encoded_text = file.read().decode("utf-8")  # Read encoded text after header

        heap = make_heap(frequency)
        merge_nodes(heap)
        root = heap[0]
        codes, reverse_mapping = make_codes(root)

        decoded_text = decode_text(encoded_text, reverse_mapping)

        with open(output_path, "w") as output:
            output.write(decoded_text)

    print("Decompressed")
    return output_path


def decode_text(encoded_text, reverse_mapping):
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_mapping:
            character = reverse_mapping[current_code]
            decoded_text += character
            current_code = ""  # Reset the code for next iteration
    return decoded_text


def compress(file_path):
    filename, file_extension = os.path.splitext(file_path)
    output_path = filename + "_compressed.bin"

    with open(file_path, "r") as file:
        text = file.read()
        text = text.rstrip()

        frequency = make_frequency_dict(text)
        heap = make_heap(frequency)
        merge_nodes(heap)
        root = heap[0]
        codes, _ = make_codes(root)

        encoded_text = get_encoded_text(text, codes)

        with open(output_path, "wb") as output:
            pickle.dump(frequency, output)  # Save frequency dictionary as header
            output.write(
                bytes(encoded_text, "utf-8")
            )  # Write encoded text after header

    print("Compressed")
    return output_path


def compress_or_decompress(file_name, operation):
    if operation.lower() == "encode":
        return compress(file_name)
    elif operation.lower() == "decode":
        return decompress(file_name)
        # return
    else:
        print("Invalid operation. Choose 'encode' or 'decode'.")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Huffman Encoding and Decoding")
    parser.add_argument("file_name", help="File name to be compressed or decompressed")
    parser.add_argument("operation", help="Operation: encode or decode")

    args = parser.parse_args()

    compressed_file = compress_or_decompress(args.file_name, args.operation)
    if compressed_file:
        print(
            f"File {args.file_name} has been {args.operation}d. Compressed file: {compressed_file}"
        )
