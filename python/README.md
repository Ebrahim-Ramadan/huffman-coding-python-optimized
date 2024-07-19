concise summary of the changes from the original repository to the fork:

1. Improved type hinting and code structure in the `HuffmanCoding` class.
2. Enhanced file handling with `with` statements for better resource management.
3. Implemented more efficient bit-level encoding and decoding processes (this is the resolve for [this issue](https://github.com/hasssanezzz/huffman-coding/issues/1) on the original repo).

    + Bit-level encoding:
    - The new version processes bits directly instead of creating a long binary string.
    - It accumulates bits into bytes, writing them to the file as soon as 8 bits are collected.
    - This approach is more memory-efficient, especially for large files, as it doesn't need to hold the entire encoded data in memory. 

    * Optimized decoding:
    - The decoder now reads one byte at a time and processes it bit by bit.
    - It builds up the Huffman code incrementally, checking against the character table after each bit.
    - This method is more efficient as it doesn't require storing the entire binary string in memory.

    - Reduced intermediate data structures:
    - The new implementation eliminates the need for intermediate string representations of binary data.
    - This reduction in data conversion and manipulation leads to faster processing and lower memory usage.

    + Direct byte manipulation:
    - The code now works directly with bytes and bit operations, which is generally faster than string manipulations.
    - It uses bitwise operations (shifting and masking) for efficient bit handling.

    * Streamlined file writing and reading:
    - The encoding process writes bytes as soon as they're ready, rather than accumulating all the data before writing.
    - The decoding process reads and processes the input file in smaller chunks, improving memory efficiency for large files.

4. Added a minimum file size check (100 bytes) before applying compression.
5. Refactored `encode_file()` and `decode_file()` methods for better performance.
6. Improved main script with clearer usage instructions and more informative output.
7. Added checks for compression effectiveness, reporting size increase if compression is unsuccessful.
