import sys
from os.path import getsize
from huffman_coding import HuffmanCoding

def print_usage():
    print("Usage:")
    print("  For compression:   python main.py <input_file> <output_file>")
    print("  For decompression: python main.py -d <input_file> <output_file>")

def main():
    args = sys.argv

    if len(args) < 3 or (len(args) > 4 and args[1] == '-d') or (len(args) > 3 and args[1] != '-d'):
        print("Invalid arguments")
        print_usage()
        return

    if args[1] == '-d':
        HuffmanCoding.decode_file(args[2], args[3])
        print(f"File decompressed: {args[3]}")
    else:
        original_size = getsize(args[1])
        HuffmanCoding.encode_file(args[1], args[2])
        compressed_size = getsize(args[2])
        
        print("Original file size:", original_size, "bytes")
        print("Compressed file size:", compressed_size, "bytes")
        
        if compressed_size < original_size:
            compression_ratio = (1 - compressed_size / original_size) * 100
            print(f"Compression ratio: {compression_ratio:.2f}%")
        else:
            print("Compression unsuccessful. The compressed file is larger than the original.")
            print(f"Size increase: {((compressed_size / original_size) - 1) * 100:.2f}%")

if __name__ == "__main__":
    main()