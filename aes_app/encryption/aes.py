""" import numpy as np

# Add your AES encryption and decryption code here...
def transform_values(input_list):
    perm = np.random.permutation(256)
    transformed = [perm[x] for x in input_list]
    return transformed, perm

def inverse_transform_values(transformed, perm):
    inv_perm = np.argsort(perm)
    original = [inv_perm[x] for x in transformed]
    return original

def shift_rows(block):
    return [
        np.roll(block[0], -1),
        np.roll(block[1], -2),
        np.roll(block[2], -3),
        np.roll(block[3], -3)
    ]

def inv_shift_rows(block):
    return [
        np.roll(block[0], 1),
        np.roll(block[1], 2),
        np.roll(block[2], 3),
        np.roll(block[3], 3)
    ]

def text_to_block(text):
    ascii_values = [ord(char) for char in text]
    return np.array([ascii_values[i:i + 4] for i in range(0, len(ascii_values), 4)], dtype=np.uint8)

def block_to_text(block):
    return ''.join(chr(x) for x in block.flatten())

def aes_encrypt(plaintext, key):
    block = text_to_block(plaintext)
    round_key = text_to_block(key)

    block = np.bitwise_xor(block, round_key)

    substituted_block, perm = transform_values(block.flatten())

    shifted_block = shift_rows(block)

    encrypted_block = np.bitwise_xor(shifted_block, round_key)

    return block_to_text(encrypted_block), perm

def aes_decrypt(encrypted_text, key,perm):
    block = text_to_block(encrypted_text)
    round_key = text_to_block(key)

    block = np.bitwise_xor(block, round_key)

    shifted_block = inv_shift_rows(block)

    shifted_block_array = np.array(shifted_block)
    substituted_block = inverse_transform_values(shifted_block_array.flatten(), perm)

    decrypted_block = np.bitwise_xor(shifted_block, round_key)

    return block_to_text(decrypted_block)
 """
import numpy as np

def text_to_block(text):
    ascii_values = [ord(char) for char in text]
    return np.array([ascii_values[i:i + 4] for i in range(0, len(ascii_values), 4)], dtype=np.uint8)

def block_to_text(block):
    return ''.join(chr(x) for x in block.flatten())

def aes_encrypt(plaintext, key, perm):
    block = text_to_block(plaintext)  # Convert plaintext to 4x4 matrix
    round_key = text_to_block(key)    # Convert key to 4x4 matrix

    # Initial round (AddRoundKey)
    block = np.bitwise_xor(block, round_key)

    # SubBytes (apply permutation)
    substituted_block = [perm[x] for x in block.flatten()]
    substituted_block = np.array(substituted_block).reshape((4, 4))  # Reshape to 4x4 matrix

    # ShiftRows
    shifted_block = [
        np.roll(substituted_block[0], 0),   # Row 0: No shift
        np.roll(substituted_block[1], -1), # Row 1: Shift left by 1
        np.roll(substituted_block[2], -2), # Row 2: Shift left by 2
        np.roll(substituted_block[3], -3)  # Row 3: Shift left by 3
    ]
    shifted_block = np.array(shifted_block)  # Convert list to numpy array

    # Final AddRoundKey
    encrypted_block = np.bitwise_xor(shifted_block, round_key)

    return block_to_text(encrypted_block)  # Convert matrix back to text


def aes_decrypt(encrypted_text, key, perm):
    block = text_to_block(encrypted_text)  # Convert ciphertext to 4x4 matrix
    round_key = text_to_block(key)         # Convert key to 4x4 matrix

    # Initial AddRoundKey
    block = np.bitwise_xor(block, round_key)

    # Inverse ShiftRows
    shifted_block = [
        np.roll(block[0], 0),  # Row 0: No shift
        np.roll(block[1], 1),  # Row 1: Shift right by 1
        np.roll(block[2], 2),  # Row 2: Shift right by 2
        np.roll(block[3], 3)   # Row 3: Shift right by 3
    ]
    shifted_block = np.array(shifted_block)  # Convert list to numpy array

    # Inverse SubBytes (reverse permutation)
    substituted_block = [np.argsort(perm)[x] for x in shifted_block.flatten()]
    substituted_block = np.array(substituted_block).reshape((4, 4))  # Reshape to 4x4 matrix

    # Final AddRoundKey
    decrypted_block = np.bitwise_xor(substituted_block, round_key)

    return block_to_text(decrypted_block)  # Convert matrix back to text

