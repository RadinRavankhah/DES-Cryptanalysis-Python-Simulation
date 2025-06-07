from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import os

def binary_str_to_bytes(bin_str):
    """Convert binary string to bytes."""
    return int(bin_str, 2).to_bytes(len(bin_str) // 8, byteorder='big')

def bytes_to_binary_str(byte_data):
    """Convert bytes to binary string."""
    return ''.join(f"{byte:08b}" for byte in byte_data)

def des_ecb_encrypt(plaintext_file, key_file, output_file, hex_output_file=None):
    # Read binary strings from files
    with open(plaintext_file, 'r') as f:
        plaintext_bin = f.read().strip()

    with open(key_file, 'r') as f:
        key_bin = f.read().strip()

    # Validate key length
    if len(key_bin) != 64:
        raise ValueError("Key must be exactly 64 bits")

    # Convert binary strings to bytes
    plaintext_bytes = binary_str_to_bytes(plaintext_bin)
    key_bytes = binary_str_to_bytes(key_bin)

    # Create DES cipher in ECB mode
    cipher = DES.new(key_bytes, DES.MODE_ECB)

    # Pad plaintext to multiple of 8 bytes
    padded_plaintext = pad(plaintext_bytes, DES.block_size)

    # Encrypt
    ciphertext_bytes = cipher.encrypt(padded_plaintext)

    # Convert ciphertext to binary string
    ciphertext_bin = bytes_to_binary_str(ciphertext_bytes)

    # Save binary output
    with open(output_file, 'w') as f:
        f.write(ciphertext_bin)
    print(f"Binary ciphertext written to {output_file}")

    # Save proper hex output (matches online tools)
    if hex_output_file:
        ciphertext_hex = ciphertext_bytes.hex()
        with open(hex_output_file, 'w') as f:
            f.write(ciphertext_hex)
        print(f"Hex ciphertext written to {hex_output_file}")

# Optional: Write inputs for testing
def write_sample_inputs():
    key = '1010101011001100110011001111000011110000111100001111000011110000'  # 64 bits
    plaintext = '01101100011011110111011001100101011001100111001001101111011011000110010001101001011100110110000101110111011001010111001101101111'  # 128 bits

    with open('differential/key.txt', 'w') as f:
        f.write(key)

    with open('differential/plaintext.txt', 'w') as f:
        f.write(plaintext)

# Usage example
if __name__ == "__main__":
    write_sample_inputs()
    des_ecb_encrypt('differential/plaintext.txt', 'differential/key.txt', 'differential/ciphertext.txt', 'differential/ciphertext_hex.txt')
